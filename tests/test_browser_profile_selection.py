import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from actions import browser_control


class BrowserProfileSelectionTests(unittest.TestCase):
    def test_prefers_default_profile_for_chromium(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "Default").mkdir(parents=True, exist_ok=True)
            (root / "Profile 1").mkdir(parents=True, exist_ok=True)

            with patch.object(browser_control, "_OS", "Windows"), patch.object(
                browser_control, "_real_profile_dir", return_value=str(root)
            ):
                profile_root, profile_dir = browser_control._resolve_browser_profile("chrome")

        self.assertEqual(profile_root, str(root))
        self.assertEqual(profile_dir, "Default")


if __name__ == "__main__":
    unittest.main()
