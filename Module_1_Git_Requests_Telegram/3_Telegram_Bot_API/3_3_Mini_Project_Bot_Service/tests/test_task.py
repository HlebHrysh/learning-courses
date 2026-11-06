import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from unittest.mock import patch, Mock
import requests
from task import fetch_crypto_rate_message

class TestCryptoService(unittest.TestCase):
    @patch("requests.get")
    def test_successful_crypto_fetch(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "bitcoin": {
                "usd": 68500.5,
                "eur": 62300.0
            }
        }
        mock_get.return_value = mock_resp

        msg = fetch_crypto_rate_message("bitcoin")
        self.assertIn("Bitcoin", msg)
        self.assertIn("$68500.5", msg)
        self.assertIn("€62300.0", msg)

    @patch("requests.get")
    def test_crypto_not_found(self, mock_get):
        mock_resp = Mock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {}
        mock_get.return_value = mock_resp

        msg = fetch_crypto_rate_message("unknown_coin")
        self.assertEqual(msg, "Криптовалюту 'unknown_coin' не знайдено.")

    @patch("requests.get")
    def test_api_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("Timeout")
        msg = fetch_crypto_rate_message("bitcoin")
        self.assertEqual(msg, "Сервіс курсів валют тимчасово недоступний. Спробуйте пізніше.")

if __name__ == '__main__':
    unittest.main()
