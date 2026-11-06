import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from task import generate_python_gitignore

class TestGitIgnore(unittest.TestCase):
    def test_default_rules(self):
        rules = generate_python_gitignore(include_env=True)
        self.assertIsInstance(rules, list, "Функція має повертати список (list)")
        self.assertIn("__pycache__/", rules, "Список має містити '__pycache__/'")
        self.assertIn("*.pyc", rules, "Список має містити '*.pyc'")
        self.assertIn("venv/", rules, "Список має містити 'venv/'")
        self.assertIn(".pytest_cache/", rules, "Список має містити '.pytest_cache/'")
        self.assertIn(".env", rules, "Якщо include_env=True, у списку має бути '.env'")

    def test_without_env(self):
        rules = generate_python_gitignore(include_env=False)
        self.assertNotIn(".env", rules, "Якщо include_env=False, у списку НЕ повинно бути '.env'")
        self.assertIn("venv/", rules, "Базові правила повинні залишатися")

if __name__ == '__main__':
    unittest.main()
