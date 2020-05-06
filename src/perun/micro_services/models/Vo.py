"""
Vo object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class Vo(ObjectWithId):

    def __init__(self, id, name, short_name):
        super().__init__(id)
        self.name = name
        self.short_name = short_name

    def __str__(self):
        return f'Vo[id: {self.id}, name: {self.name}, shortName: {self.short_name}]'
