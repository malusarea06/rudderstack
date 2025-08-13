import sys
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa", help="Environment to run tests against (e.g. qa, dev, staging, prod)"
    )
    parser.addoption(
        "--browser_op", action="store", default="chromium", help="Browser to run tests (e.g. chromium, firefox, chrome)"
    )
