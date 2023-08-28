#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""

    for encoding in data:
        if encoding < 0 or encoding > 255:
            return False

    return True
