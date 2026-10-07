"""Publier la sortie HTML complète, lisible (0644), sans exposer ses versions intermédiaires."""
from contextlib import contextmanager
import os
from pathlib import Path
import tempfile


@contextmanager
def atomic_output(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, staging = tempfile.mkstemp(prefix='.medina-stage-', suffix='.html', dir=destination.parent)
    try:
        try:
            os.fchmod(descriptor, 0o644)
        finally:
            os.close(descriptor)
        yield staging
        os.replace(staging, destination)
    finally:
        if os.path.exists(staging):
            os.unlink(staging)

