#!/usr/bin/env python3
"""
Unittest module for testing GithubOrgClient
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test class for GithubOrgClient.public_repos
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def get_side_effect(url):
            """
            Side effect function to return payloads based on URL
            """
            if url == "https://api.github.com/orgs/google":
                return cls.org_payload
            if url == "https://api.github.com/orgs/google/repos":
                return cls.repos_payload

        cls.mock_get.side_effect = lambda url: Mock(json=get_side_effect(url))

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test that public_repos returns the correct list of repos
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)


if __name__ == '__main__':
    unittest.main()
