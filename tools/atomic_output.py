"""Publier un fichier construit sans exposer ses versions intermédiaires."""
from contextlib import contextmanager
import os
from pathlib import Path
import stat
import tempfile


@contextmanager
def atomic_output(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(destination.stat().st_mode) if destination.exists() else 0o644
    descriptor, staging = tempfile.mkstemp(prefix='.medina-stage-', suffix='.html', dir=destination.parent)
    try:
        os.fchmod(descriptor, mode)
    finally:
        os.close(descriptor)
    try:
        yield staging
        os.replace(staging, destination)
    finally:
        if os.path.exists(staging):
            os.unlink(staging)
