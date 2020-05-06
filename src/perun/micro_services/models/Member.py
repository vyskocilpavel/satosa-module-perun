"""
Member object
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.models.ObjectWithId import ObjectWithId


class Member(ObjectWithId):

    VALID = 'VALID'
    INVALID = 'INVALID'
    EXPIRED = 'EXPIRED'
    SUSPENDED = 'SUSPENDED'
    DISABLED = 'DISABLED'

    MEMBER_STATES = [VALID, INVALID, EXPIRED, SUSPENDED, DISABLED]

    def __init__(self, id, vo_id, status):
        super().__init__(id)
        self.vo_id = vo_id
        self.status = status

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, value):
        if value not in self.MEMBER_STATES:
            raise ValueError(f'Value {value} cannot be assigned as member status. '
                             f'You must assign one of {self.MEMBER_STATES}')

    def __str__(self):
        return f'Member[id: {self.id}, vo_id: {self.vo_id}, status: {self.status}]'
