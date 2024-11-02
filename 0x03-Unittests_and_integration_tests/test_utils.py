#!/usr/bin/env python3
"""Unittest module for memoize decorator."""

import unittest
from unittest.mock import patch
from utils import memoize


class TestClass:
    """Test class for memoize tests"""

    def a_method(self) -> int:
        """Returns the number 42."""
        return 42

    @memoize
    def a_property(self) -> int:
        """Returns the memoized result of a_method."""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test memoize functionality"""
        test_instance = TestClass()

        with patch.object(test_instance, 'a_method',
                          return_value=42) as mock_method:
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
