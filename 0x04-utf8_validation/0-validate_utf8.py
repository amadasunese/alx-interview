#!/usr/bin/python3
""" A method that determines valid UTF-8 encoding """


def validUTF8(data):
    """ A method that determines valid UTF-8 encoding """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
