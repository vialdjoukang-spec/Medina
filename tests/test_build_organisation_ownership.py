"""The public dashboard must agree with the isolated specialty frontend."""
import unittest

from tools.build_organisation import load_data


class OrganisationOwnershipTests(unittest.TestCase):
    def test_transferred_infectious_categories_stay_in_infectiology(self):
        data = load_data("2026-10-08T00:00:00Z")
        categories = {
            fragment["id"]: {
                row["code"]
                for block in fragment["blocks"]
                for row in block["categories"]
            }
            for fragment in data["fragments"]
        }
        self.assertTrue({"A04", "A43", "B18"}.issubset(categories["T1"]))
        self.assertTrue({"A04", "B18"}.isdisjoint(categories["S03"]))


if __name__ == "__main__":
    unittest.main()
