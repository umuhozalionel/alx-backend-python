#!/usr/bin/env python3
"""
Unittest module for testing GithubOrgClient
"""

import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the expected value
        """
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }

        client = GithubOrgClient('google')
        result = client._public_repos_url

        self.assertEqual(result, 'https://api.github.com/orgs/google/repos')


if __name__ == '__main__':
    unittest.main()
