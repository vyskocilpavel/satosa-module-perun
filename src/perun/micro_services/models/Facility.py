"""
Facility object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class Facility(ObjectWithId):

    def __init__(self, id, name, description, entity_id):
        super().__init__(id)
        self.name = name
        self.description = description
        self.entity_id = entity_id

    def __str__(self):
        return f'Facility[id: {self.id}, name: {self.name}, description: {self.description}, ' \
               f'entityId: {self.entity_id}]'
