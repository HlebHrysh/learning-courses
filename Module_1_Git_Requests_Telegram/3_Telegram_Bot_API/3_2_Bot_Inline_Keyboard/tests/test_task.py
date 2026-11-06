import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from task import build_inline_keyboard

class TestInlineKeyboard(unittest.TestCase):
    def test_two_columns_layout(self):
        items = [
            ("Python", "lang_py"),
            ("JavaScript", "lang_js"),
            ("Docker", "tool_docker")
        ]
        kb = build_inline_keyboard(items, columns=2)
        expected = [
            [{"text": "Python", "callback_data": "lang_py"}, {"text": "JavaScript", "callback_data": "lang_js"}],
            [{"text": "Docker", "callback_data": "tool_docker"}]
        ]
        self.assertEqual(kb, expected)

    def test_single_column_layout(self):
        items = [("Кнопка 1", "cb1"), ("Кнопка 2", "cb2")]
        kb = build_inline_keyboard(items, columns=1)
        expected = [
            [{"text": "Кнопка 1", "callback_data": "cb1"}],
            [{"text": "Кнопка 2", "callback_data": "cb2"}]
        ]
        self.assertEqual(kb, expected)

if __name__ == '__main__':
    unittest.main()
