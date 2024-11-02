#!/usr/bin/env python3
"""Unittest module for GithubOrgClient."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_instance = GithubOrgClient(org_name)
        mock_get_json.return_value = {"org": org_name}
        
        response = test_instance.org
        self.assertEqual(response, {"org": org_name})
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}
        test_instance = GithubOrgClient("google")
        
        result = test_instance._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
