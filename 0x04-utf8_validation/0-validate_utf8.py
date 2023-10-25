#!/usr/bin/env python3
"""
A method that determines valid UTF-8 encoding
"""


def validUTF8(data):
    # Initialize the number of bytes needed for the current character
    bytes_needed = 0

    # Iterate through each byte in the data set
    for byte in data:
        # Check if the current byte is a continuation byte (10xxxxxx)
        if byte >> 6 == 0b10:
            # If the current byte is a continuation byte, it means that the previous byte was a start byte (0xxxxxxx or 11xxxxxx)
            # Therefore, we need to decrement the number of bytes needed for the current character
            bytes_needed -= 1

            # If the number of bytes needed for the current character is negative, it means that the previous byte was not a start byte
            # Therefore, the data set is not a valid UTF-8 encoding
            if bytes_needed < 0:
                return False
        else:
            # If the current byte is not a continuation byte, it means that it is a start byte (0xxxxxxx or 11xxxxxx)
            # Therefore, we need to determine the number of bytes needed for the current character
            bytes_needed = 0
            while byte & 0b10000000 == 0b10000000:
                bytes_needed += 1
                byte <<= 1

            # If the number of bytes needed for the current character is greater than 4, it means that the start byte was not valid
            # Therefore, the data set is not a valid UTF-8 encoding
            if bytes_needed > 4:
                return False

    # If the number of bytes needed for the current character is not 0, it means that the last start byte was not followed by enough continuation bytes
    # Therefore, the data set is not a valid UTF-8 encoding
    if bytes_needed != 0:
        return False

    # If none of the above conditions were met, the data set is a valid UTF-8 encoding
    return True