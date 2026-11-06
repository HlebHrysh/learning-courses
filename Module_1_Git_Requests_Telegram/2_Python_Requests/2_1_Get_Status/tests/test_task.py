import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from unittest.mock import patch, Mock
import requests
from task import check_service_status

class TestGetStatus(unittest.TestCase):
    @patch("requests.get")
    def test_success_200(self, mock_get):
        mock_resp = Mock()
        mock_resp.ok = True
        mock_resp.status_code = 200
        mock_get.return_value = mock_resp

        result = check_service_status("https://example.com/api")
        self.assertEqual(result, {"is_online": True, "status_code": 200})

    @patch("requests.get")
    def test_client_error_404(self, mock_get):
        mock_resp = Mock()
        mock_resp.ok = False
        mock_resp.status_code = 404
        mock_get.return_value = mock_resp

        result = check_service_status("https://example.com/notfound")
        self.assertEqual(result, {"is_online": False, "status_code": 404})

    @patch("requests.get")
    def test_network_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("Connection refused")
        result = check_service_status("https://invalid-host-404.ua")
        self.assertEqual(result, {"is_online": False, "status_code": None})

if __name__ == '__main__':
    unittest.main()
