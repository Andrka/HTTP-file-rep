# -*- coding:utf-8 -*-

"""Test values module."""

import pytest

from http_file_repo import values

@pytest.mark.parametrize(
    'sample_value, expected_result',
    [
        ('', False),
        ('bfb372a7ac3f9dbacce362346d82a2e0', True),
        ('Bfb372a7ac3f9dbacce362346d82a2e0', False),
        ('bfb372a7ac3f9dbacce362346d82a2e00', False),
        ('bfb372a7ac3f9dbacce362346d82a2e', False),
    ],
)
def test_is_correct_hash(sample_value, expected_result):
    """Test is_correct_hash function."""
    assert values.is_correct_hash(sample_value) == expected_result
