#!/usr/bin/env python3
"""Root CLI shortcut for PrepIntel with automatic virtualenv site-packages detection."""

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent

# Ensure .venv site-packages is in sys.path if not activated
venv_site = list(root_dir.glob(".venv/lib/python*/site-packages"))
if venv_site and str(venv_site[0]) not in sys.path:
    sys.path.insert(0, str(venv_site[0]))

tools_dir = root_dir / "tools"
if str(tools_dir) not in sys.path:
    sys.path.insert(0, str(tools_dir))

from prep_intel.ui.cli import main

if __name__ == "__main__":
    main()
