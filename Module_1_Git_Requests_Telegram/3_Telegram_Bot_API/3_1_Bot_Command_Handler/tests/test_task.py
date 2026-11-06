import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from task import dispatch_telegram_message

class TestBotCommands(unittest.TestCase):
    def test_start_command(self):
        msg = dispatch_telegram_message("/start", "Гліб")
        self.assertEqual(msg, "Вітаю, Гліб! Я ваш навчальний бот-асистент.")

    def test_help_command(self):
        msg = dispatch_telegram_message("/help", "Гліб")
        self.assertIn("/weather", msg)
        self.assertIn("/rates", msg)

    def test_weather_command(self):
        msg = dispatch_telegram_message("/weather", "Гліб")
        self.assertEqual(msg, "Для отримання погоди введіть назву міста.")

    def test_unknown_command(self):
        msg = dispatch_telegram_message("/random_xyz", "Гліб")
        self.assertIn("Невідома команда", msg)

if __name__ == '__main__':
    unittest.main()
