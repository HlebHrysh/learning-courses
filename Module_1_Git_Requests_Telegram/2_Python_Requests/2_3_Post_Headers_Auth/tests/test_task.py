import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import unittest
from unittest.mock import patch, Mock
from task import create_remote_post

class TestPostHeadersAuth(unittest.TestCase):
    @patch("requests.post")
    def test_successful_creation(self, mock_post):
        mock_resp = Mock()
        mock_resp.status_code = 201
        mock_resp.json.return_value = {"id": 101, "title": "Привіт Світ"}
        mock_post.return_value = mock_resp

        res = create_remote_post("https://api.org/posts", "my_secret_token", "Привіт Світ", "Текст поста")
        mock_post.assert_called_with(
            "https://api.org/posts",
            json={"title": "Привіт Світ", "content": "Текст поста"},
            headers={"Authorization": "Bearer my_secret_token"}
        )
        self.assertEqual(res, {"success": True, "data": {"id": 101, "title": "Привіт Світ"}})

    @patch("requests.post")
    def test_unauthorized_error(self, mock_post):
        mock_resp = Mock()
        mock_resp.status_code = 401
        mock_post.return_value = mock_resp

        res = create_remote_post("https://api.org/posts", "bad_token", "Тест", "Опис")
        self.assertEqual(res, {"success": False, "status_code": 401})

if __name__ == '__main__':
    unittest.main()
