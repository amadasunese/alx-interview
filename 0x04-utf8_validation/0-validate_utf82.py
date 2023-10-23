#!/usr/bin/python3
"""
A method that determine a valid UTF-8 encoding.
"""
def validUTF8(data):
  """
  Determines if a given data set represents a valid UTF-8 encoding.

  Args:
    data: A list of integers, where each integer represents one byte of data.

  Returns:
    True if data is a valid UTF-8 encoding, else return False.
  """

  # Check if the data is empty.
  if not data:
    return False

  # Initialize the state of the decoder.
  state = 0

  # Iterate over the data.
  for byte in data:
    # Get the 8 least significant bits of the byte.
    byte = byte & 0xFF

    # If the state is 0, then we are expecting the start of a new character.
    if state == 0:
      # If the byte is a start byte, then transition to the next state.
      if byte >= 0xC0 and byte <= 0xDF:
        state = 1
      # If the byte is not a start byte, then the data is invalid.
      else:
        return False
    # If the state is not 0, then we are expecting a continuation byte.
    else:
      # If the byte is not a continuation byte, then the data is invalid.
      if byte < 0x80 or byte > 0xBF:
        return False
      # Otherwise, transition to the next state.
      state += 1

      # If we have reached the end of a character, then reset the state.
      if state == 4:
        state = 0

  # If we reach the end of the data while in a non-zero state, then the data is invalid.
  if state != 0:
    return False

  # Otherwise, the data is a valid UTF-8 encoding.
  return True
