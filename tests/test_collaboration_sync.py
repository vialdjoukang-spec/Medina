"""Contrôles du scan interbranches ; données synthétiques, aucun réseau."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("collaboration_sync", Path(__file__).resolve().parents[1] / "tools/collaboration_sync.py")
SYNC = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SYNC)


def catalog():
    return {"chapters": {"I48": {"code": "I48", "integrated": True}},
            "systems": {"I48": "Cœur"},
            "fragments": [{"id": "S01", "rattachements": ["Cœur", "I48"], "surface": "courses-v1",
                           "categories": [{"chapters": ["I48"]}]}]}


def snapshot():
    return {"repository": "test/Medina", "integration_branch": "integration", "integration_commit": "t" * 40,
            "branches": [{"name": "integration", "commit": {"sha": "t" * 40}},
                         {"name": "claude/review", "commit": {"sha": "c" * 40}}],
            "pull_requests": [], "comparisons": {}, "scan_complete": True}


class CollaborationSyncTests(unittest.TestCase):
    def test_pagination_has_no_first_page_limit(self):
        calls = []
        def request(path, params):
            calls.append(params["page"])
            return list(range(100)) if params["page"] == 1 else [100, 101]
        self.assertEqual(len(SYNC.GitHubClient("test/repo", request=request).pages("/branches")), 102)
        self.assertEqual(calls, [1, 2])

    def test_collect_paginates_branches_prs_and_pr_files(self):
        calls = []
        branch = {"name": "integration", "commit": {"sha": "t" * 40}}
        pr = {"number": 1, "head": {"sha": "c" * 40, "ref": "review"}, "base": {"ref": "integration"}}
        def request(path, params=None):
            calls.append((path, params))
            page = (params or {}).get("page", 1)
            if path == "/branches":
                return [branch] * 100 if page == 1 else [{"name": "review", "commit": {"sha": "c" * 40}}]
            if path == "/pulls":
                return [pr] * 100 if page == 1 else []
            if path == "/pulls/1/files":
                return [{"filename": "chapters/I48/I48_a.html", "status": "modified"}] * 100 if page == 1 else []
            if path.startswith("/compare/"):
                return {"status": "ahead", "files": []}
            if path == "/contents/docs/collaboration/receipts":
                return []
            if path.startswith("/contents/"):
                return {"encoding": "base64", "content": "W10=", "sha": "x" * 40}
            raise AssertionError(path)
        result = SYNC.GitHubClient("test/repo", request=request).collect("integration")
        self.assertEqual(len(result["branches"]), 101)
        self.assertEqual(len(result["pull_requests"]), 100)
        self.assertTrue(any(p == "/pulls" and q["page"] == 2 for p, q in calls))
        self.assertTrue(any(p.endswith("/files") and q["page"] == 2 for p, q in calls))

    def test_received_head_does_not_mean_integrated(self):
        data = snapshot()
        data["receipts"] = [{"head_sha": "c" * 40, "received_at": "2026-10-07", "integration_commit": "x" * 40}]
        delivery = SYNC.build_report(data, catalog())["deliveries"][0]
        self.assertTrue(delivery["received"])
        self.assertFalse(delivery["integrated"])
        self.assertFalse(delivery["verified"])

    def test_ancestor_integrated_but_not_automatically_verified(self):
        data = snapshot()
        data["comparisons"]["c" * 40] = {"status": "behind", "files": []}
        delivery = SYNC.build_report(data, catalog())["deliveries"][0]
        self.assertTrue(delivery["integrated"])
        self.assertFalse(delivery["received"])
        self.assertFalse(delivery["verified"])

    def test_cherry_pick_requires_target_proof_and_checks(self):
        data = snapshot()
        data["receipts"] = [{"head_sha": "c" * 40, "received_at": "2026-10-07",
                             "integration_commit": "t" * 40, "verification_commit": "t" * 40,
                             "checks": [{"command": "existing checks", "passed": True}]}]
        delivery = SYNC.build_report(data, catalog())["deliveries"][0]
        self.assertTrue(delivery["integrated"])
        self.assertTrue(delivery["verified"])
        data["receipts"][0]["checks"][0]["passed"] = False
        self.assertFalse(SYNC.build_report(data, catalog())["deliveries"][0]["verified"])

    def test_unproven_integration_receipt_does_not_verify_ancestor(self):
        data = snapshot()
        data["comparisons"]["c" * 40] = {"status": "behind", "files": []}
        data["receipts"] = [{"head_sha": "c" * 40, "received_at": "2026-10-07",
                             "integration_commit": "x" * 40, "verification_commit": "x" * 40,
                             "checks": [{"passed": True}]}]
        delivery = SYNC.build_report(data, catalog())["deliveries"][0]
        self.assertTrue(delivery["integrated"])
        self.assertFalse(delivery["verified"])

    def test_routing_i48_cs_derived_and_legacy_flat_report(self):
        self.assertEqual(SYNC.route_file("chapters/I48/I48_pop2.html", catalog())["routes"], ["S01"])
        self.assertEqual(SYNC.route_file("modules/cardiovascular_cs.js", catalog())["routes"], ["S01", "CS"])
        self.assertEqual(SYNC.route_file("dist/MEDINA_final.html", catalog())["kind"], "derived")
        report = SYNC.route_file("docs/collaboration/reviews/I48_ESC2024.md", catalog())
        self.assertEqual(report["kind"], "review_report")
        self.assertEqual(report["course"], "I48")

    def test_delivery_sources_route_to_their_canonical_fragment(self):
        route = SYNC.route_file("livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/I48/I48_c.html", catalog())
        self.assertEqual(route["routes"], ["S01"])
        self.assertEqual(route["canonical_path"], "chapters/I48/I48_c.html")
        self.assertEqual(route["kind"], "delivery_source")
        self.assertTrue(any("injecter" in warning for warning in route["warnings"]))
        self.assertEqual(SYNC.route_file("livraisons/Livraison Claude/C-01-Cardiologie/livraison.json", catalog())["kind"], "delivery_report")

    def test_unknown_path_absent_registration_and_wrong_category(self):
        self.assertTrue(SYNC.route_file("unwired/new_course.json", catalog())["warnings"])
        missing = SYNC.route_file("chapters/J99/J99_a.html", catalog())
        self.assertTrue(any("chapters.json" in w for w in missing["warnings"]))
        broken = catalog()
        broken["fragments"][0]["categories"] = []
        self.assertTrue(any("exactement une fois" in w for w in SYNC.route_file("chapters/I48/I48_a.html", broken)["warnings"]))
        self.assertTrue(any("zz_fusion" in w for w in SYNC.route_file("glossary/i48.py", catalog())["warnings"]))
        self.assertTrue(any("Adaptateur" in w for w in SYNC.route_file("modules/systems/cardiovascular/normal.json", catalog())["warnings"]))

    def test_fragment_audit_name_precedes_ambiguous_cim_code(self):
        ambiguous = catalog()
        ambiguous["chapters"]["S01"] = {"code": "S01", "integrated": True}
        ambiguous["fragments"].append({"id": "T3", "rattachements": ["S01"]})
        audit = SYNC.route_file("audits/S01_2026-10-05/browser-results.json", ambiguous)
        self.assertEqual(audit["routes"], ["S01"])
        self.assertNotIn("course", audit)
        self.assertEqual(SYNC.route_file("chapters/S01/S01_a.html", ambiguous)["routes"], ["T3"])
        self.assertEqual(SYNC.route_file("docs/collaboration/reviews/CS_2026-10-07.md", ambiguous)["routes"], ["S01", "CS"])

    def test_site_templates_are_consultation_sources(self):
        for path in ("site/index_template.html", "site/qcm.html"):
            result = SYNC.route_file(path, catalog())
            self.assertEqual(result["kind"], "consultation_source")
            self.assertEqual(result["routes"], ["GLOBAL"])
            self.assertFalse(result["warnings"])

    def test_pr_without_comparison_stays_unintegrated(self):
        data = snapshot()
        data["pull_requests"] = [{"number": 8, "head": {"sha": "c" * 40, "ref": "claude/review"},
                                  "base": {"ref": "main"}, "state": "closed", "merged_at": "2026-10-07",
                                  "files": [{"filename": "chapters/I48/I48_a.html", "status": "modified"}]}]
        delivery = SYNC.build_report(data, catalog())["deliveries"][0]
        self.assertFalse(delivery["integrated"])
        self.assertEqual(delivery["files"][0]["diff_basis"], "pull_request_base")
        self.assertTrue(any("vise main" in w for w in delivery["warnings"]))

    def test_snapshot_cli_is_offline_and_writes_only_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "chapters.json").write_text(json.dumps(list(catalog()["chapters"].values())))
            (root / "fragments.json").write_text(json.dumps(catalog()["fragments"]))
            source = root / "snapshot.json"
            source.write_text(json.dumps(snapshot()))
            old_collect = SYNC.GitHubClient.collect
            SYNC.GitHubClient.collect = lambda *args: self.fail("Réseau déclenché en mode snapshot")
            try:
                self.assertEqual(SYNC.main(["--snapshot", str(source), "--root", str(root), "--out", str(root / "out")]), 0)
            finally:
                SYNC.GitHubClient.collect = old_collect
            self.assertTrue((root / "out/DELIVERIES_LATEST.md").exists())
            self.assertEqual(json.loads((root / "out/DELIVERIES_LATEST.json").read_text())["integration_branch"], "integration")
            self.assertEqual(set(p.name for p in root.iterdir()), {"chapters.json", "fragments.json", "snapshot.json", "out"})

    def test_local_catalog_uses_target_commit_not_current_branch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.DEVNULL, text=True).strip()
            git("init")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            (root / "chapters.json").write_text(json.dumps(list(catalog()["chapters"].values())))
            (root / "fragments.json").write_text(json.dumps(catalog()["fragments"]))
            git("add", "chapters.json", "fragments.json")
            git("commit", "-m", "Target catalog")
            sha = git("rev-parse", "HEAD")
            (root / "chapters.json").write_text("[]")
            pinned = SYNC.load_catalog(root, sha)
            self.assertIn("I48", pinned["chapters"])
            self.assertEqual(pinned["basis"], "git:" + sha)

    def test_committed_target_receipt_survives_local_pr_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                return subprocess.check_output(["git", "-C", str(root), *args], stderr=subprocess.DEVNULL, text=True).strip()
            git("init")
            git("config", "user.name", "Test")
            git("config", "user.email", "test@example.invalid")
            folder = root / "docs/collaboration/receipts"
            folder.mkdir(parents=True)
            receipt = folder / "CLAUDE-I48.json"
            receipt.write_text(json.dumps({"head_sha": "c" * 40, "received_at": "2026-10-07"}))
            git("add", "docs")
            git("commit", "-m", "Target receipt")
            target = git("rev-parse", "HEAD")
            receipt.write_text(json.dumps({"head_sha": "c" * 40, "received_at": None}))
            records, notes = SYNC.load_receipts(root, target)
            self.assertEqual(records[0]["received_at"], "2026-10-07")
            self.assertFalse(notes)
            data = snapshot()
            data["receipts"] = records
            self.assertTrue(SYNC.build_report(data, catalog())["deliveries"][0]["received"])

    def test_github_receipts_read_at_target_sha(self):
        calls = []
        def request(path, params=None):
            calls.append((path, params))
            return [{"path": "docs/collaboration/receipts/I48.json", "type": "file"}]
        client = SYNC.GitHubClient("test/repo", request=request)
        client.content = lambda path, commit: json.dumps({"head_sha": "c" * 40, "received_at": "2026-10-07"}).encode()
        records, notes, complete = client.receipts("t" * 40)
        self.assertEqual(calls[0][1], {"ref": "t" * 40})
        self.assertTrue(records[0]["received_at"])
        self.assertTrue(complete)
        self.assertFalse(notes)


if __name__ == "__main__":
    unittest.main()
