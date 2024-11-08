#!/usr/bin/env python3
"""
Unittest module for testing get_json
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test get_json returns expected result
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock(**{"json.return_value": test_payload})

            response = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)


if __name__ == '__main__':
    unittest.main()
