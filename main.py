import sys
from pathlib import Path
import importlib.util

backend_dir = Path(__file__).resolve().parent / "backend"
sys.path.insert(0, str(backend_dir))

backend_main = backend_dir / "main.py"

spec = importlib.util.spec_from_file_location("backend_main", backend_main)
backend = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backend)

app = backend.app
