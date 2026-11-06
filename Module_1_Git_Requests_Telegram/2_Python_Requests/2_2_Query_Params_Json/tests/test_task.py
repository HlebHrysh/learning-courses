import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from unittest.mock import patch, Mock
from task import filter_active_users

class TestQueryParamsJson(unittest.TestCase):
    @patch("requests.get")
    def test_filter_users(self, mock_get):
        mock_resp = Mock()
        mock_resp.json.return_value = [
            {"username": "bohdan", "rating": 4.9},
            {"username": "iryna", "rating": 3.2},
            {"username": "taras", "rating": 4.5},
            {"username": "katya", "rating": 4.0}
        ]
        mock_get.return_value = mock_resp

        result = filter_active_users("https://api.test.ua/users", 4.2)
        mock_get.assert_called_with("https://api.test.ua/users", params={"status": "active"})
        self.assertEqual(result, ["bohdan", "taras"])

if __name__ == '__main__':
    unittest.main()
