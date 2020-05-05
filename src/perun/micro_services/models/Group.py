"""
Group Object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class Group(ObjectWithId):

    def __init__(self, id, vo_id, name, description, entity_id):
        super().__init__(id)
        self.vo_id = vo_id
        self.name = name
        self.description = description
        self.unique_name = entity_id

    def __str__(self):
        return f'Group[id: {self.id}, vo_id:{self.vo_id}, name:{self.name}, ' \
               f'description:{self.description}, uniqueName:{self.unique_name}]'
