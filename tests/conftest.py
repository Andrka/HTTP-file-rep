# -*- coding:utf-8 -*-

"""Define fixtures to use in tests."""

import pytest

from http_file_repo.app import app


@pytest.fixture
def client():
    """Define client for tests."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
