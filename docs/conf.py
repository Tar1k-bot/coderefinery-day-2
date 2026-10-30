import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

project = "example"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

exclude_patterns = ["_build"]
root_doc = "index"
html_theme = "nature"
