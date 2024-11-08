#!/usr/bin/env python3
"""
Unittest module for testing GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value
        """
        expected_value = {"org_name": org_name}
        mock_get_json.return_value = expected_value

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
