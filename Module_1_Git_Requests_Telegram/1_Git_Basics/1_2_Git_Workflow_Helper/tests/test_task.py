import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from task import validate_commit_message

class TestGitCommitValidator(unittest.TestCase):
    def test_valid_messages(self):
        self.assertTrue(validate_commit_message("feat: add telegram auth"))
        self.assertTrue(validate_commit_message("fix: resolve timeout error"))
        self.assertTrue(validate_commit_message("docs: update README guide"))
        self.assertTrue(validate_commit_message("refactor: split api module"))

    def test_invalid_prefixes(self):
        self.assertFalse(validate_commit_message("custom: something changed"))
        self.assertFalse(validate_commit_message("added new feature"))
        self.assertFalse(validate_commit_message("feat without colon"))

    def test_too_short(self):
        self.assertFalse(validate_commit_message("feat: ab"))
        self.assertFalse(validate_commit_message("fix: "))

if __name__ == '__main__':
    unittest.main()
