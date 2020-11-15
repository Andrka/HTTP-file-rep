# -*- coding:utf-8 -*-

"""Check if values are correct."""

import re

HASH_REGEX = r'\b([a-f\d]{32}|[A-F\d]{32})\b'


def is_correct_hash(file_hash):
    """Check if given string is md5 hash."""
    correct_parts = re.findall(HASH_REGEX, file_hash)
    if not correct_parts:
        correct_parts.append('-')
    return file_hash == correct_parts[0]
