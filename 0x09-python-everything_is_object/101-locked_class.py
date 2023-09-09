#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    stops the user from dynamically  new LockedClass attributes
    for anything but attributes called first_name.
    """

    __slots__ = ["first_name"]
