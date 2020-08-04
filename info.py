"""
This docstring should be right below the class declaration line.
"""
"""
This is the key class used in the text message response code. It contains the text of the message sent, the phone numbers, and the info dict about the restaurant.
"""

"""
Class names should use UpperCamelCase (this class should be named Info)
"""
class info:

    def __init__(self, txt, fro, to, rinfo):
        self.txt = txt
        self.fro = fro
        self.to = to
        self.rinfo = rinfo

