"""
Interface for object with Id
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from abc import ABC


class ObjectWithId(ABC):

    def __init__(self, id):
        self.id = id
