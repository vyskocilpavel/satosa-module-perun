"""
User object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class User(ObjectWithId):

    def __init__(self, id, name):
        super().__init__(id)
        self.name = name

    def __str__(self):
        return f'User[id: {self.id}, name: {self.name}]'
