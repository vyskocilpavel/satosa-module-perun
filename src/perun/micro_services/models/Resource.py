"""
Resource Object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class Resource(ObjectWithId):

    def __init__(self, id, vo_id, facility_id, name):
        super().__init__(id)
        self.vo_id = vo_id
        self.facility_id = facility_id
        self.name = name

    def __str__(self):
        return f'Resource[id: {self.id}, vo_id: {self.vo_id}, facilityId: {self.facility_id}, name: {self.name}]'
