#!/usr/bin/env python3
"""
Tests for client module
"""
import unittest
from unittest import mock
from unittest.mock import PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True}),
    ])
    @mock.patch("client.get_json")
    def test_org(self, url, payload, mock_get_json):
        """
        Test GithubOrgClient
        """
        mock_get_json.return_value = payload
        g_client = GithubOrgClient(url)
        res = g_client.org
        self.assertEqual(res, payload)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        Test public_repos_url
        """
        with mock.patch.object(GithubOrgClient,
                               "org",
                               new_callable=PropertyMock) as mock_org:
            test_json = {"url": "facebook", "repos_url": "http://testurl.com"}
            mock_org.return_value = test_json
            g_client = GithubOrgClient(test_json.get("url"))
            res = g_client._public_repos_url
            mock_org.assert_called_once()
            self.assertEqual(res, test_json.get("repos_url"))

    @mock.patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos
        """
        mock_get_json.return_value = [{"name": "google"},
                                      {"name": "abc"}]
        with mock.patch.object(GithubOrgClient, "_public_repos_url",
                               new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "http://testurl.com"
            g_client = GithubOrgClient("facebook")
            res = g_client.public_repos()
            self.assertEqual(res, ["google", "abc"])
            mock_get_json.assert_called_once()
            mock_public.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """
        Test for test_has_license
        """
        g_client = GithubOrgClient("facebook")
        res = (g_client.has_license(repo, license))
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
