#!/usr/bin/python3
"""
A method that determines valid UTF-8 encoding
"""


def validUTF8(data):
    """Initialize a variable to keep track of the number of remaining bytes
    """
    remaining_bytes = 0

    # Iterate through each integer in the data list
    for num in data:
        # Check if the number is a valid UTF-8 start byte
        if remaining_bytes == 0:
            if (num >> 7) == 0b0:
                remaining_bytes = 0
            elif (num >> 5) == 0b110:
                remaining_bytes = 1
            elif (num >> 4) == 0b1110:
                remaining_bytes = 2
            elif (num >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                return False
        else:
            # Check if the current number is a valid continuation byte
            if (num >> 6) == 0b10:
                remaining_bytes -= 1
            else:
                return False

    # If there are remaining bytes after processing all integers, it's invalid
    return remaining_bytes == 0
