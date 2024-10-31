#!/usr/bin/python3
"""
utf8_validation.py

This module provides a utility function to validate UTF-8 encoding.

The `validUTF8` function examines a list of integers, where each
integer represents a byte in a sequence.
It checks whether the sequence conforms to the UTF-8 encoding
scheme, ensuring that each character's byte pattern is correct.
"""


def validUTF8(data: list[int]) -> bool:
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    Each integer in the dataset represents a byte in a UTF-8 sequence,
    with valid UTF-8 characters requiring between 1 and 4 bytes.
    This function verifies that each byte conforms to UTF-8 encoding rules.

    Parameters:
    - data: List[int] - a list of integers, where each integer
            represents 1 byte (0-255).

    Returns:
    - bool: True if the dataset is valid UTF-8 encoding, False otherwise.

    Example:
    >>> validUTF8([197, 130, 1])  # Valid UTF-8 encoding for "Å" (U+00C5)
    True
    >>> validUTF8([235, 140, 4])  # Invalid sequence
    False
    """
    n_bytes = 0

    for num in data:
        # Ensure byte is within the valid range for UTF-8 (0-255).
        if num < 0 or num > 255:
            return False

        # Start of a new UTF-8 character
        if n_bytes == 0:
            if (num >> 7) == 0b0:
                # 1-byte character (ASCII), n_bytes remains 0
                continue
            elif (num >> 5) == 0b110:
                # 2-byte character
                n_bytes = 1
            elif (num >> 4) == 0b1110:
                # 3-byte character
                n_bytes = 2
            elif (num >> 3) == 0b11110:
                # 4-byte character
                n_bytes = 3
            else:
                # Invalid leading byte
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (num >> 6) != 0b10:
                return False

            n_bytes -= 1

    # Ensure there are no leftover expected continuation bytes
    return n_bytes == 0
