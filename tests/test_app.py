# -*- coding:utf-8 -*-

"""Test app module."""

from io import BytesIO

import pytest


@pytest.mark.parametrize(
    'sample_file, file_name, file_hash',
    [
        (b'\xc3\x96l\xc3\x96l', 'sample.txt', '77ef24eaa0fc1ab5f21b040638cf6ef8'),
        (b'\xE2\x82\xAC', '0', 'bca53fde466a76b7bee3e18997e94a7a'),
    ],
)
def test_http_api(client, sample_file, file_name, file_hash):
    """Test HTTP API."""

    def test_upload(client, sample_file, file_name, file_hash):
        """Test file upload."""
        global new_hash
        data = {
            'file': (
                BytesIO(sample_file),
                file_name,
            ),
        }
        res = client.post('/upload', data=data)
        new_hash = res.json['hash']
        assert res.status_code == 200
        assert new_hash == file_hash

    def test_download(client, new_hash):
        """Test file download."""
        url = '/download/{0}'.format(new_hash)
        res = client.get(url)
        assert res.status_code == 200

    def test_delete(client, new_hash):
        """Test file delete."""
        url = '/delete/{0}'.format(new_hash)
        res = client.delete(url)
        assert res.status_code == 200

    test_upload(client, sample_file, file_name, file_hash)
    test_download(client, new_hash)
    test_delete(client, new_hash)
