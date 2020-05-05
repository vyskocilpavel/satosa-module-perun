"""
Abstract class PerunAdapterAbstract
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from abc import ABC, abstractmethod


class PerunAdapterAbstract(ABC):

    LDAP = 'ldap'
    RPC = 'rpc'

    @abstractmethod
    def get_perun_user(self, idp_entity_id, uids):
        pass

    @abstractmethod
    def get_facility_by_entity_id(self, entity_id):
        pass

    @abstractmethod
    def get_user_groups_on_facility(self, user, facility):
        pass

    @abstractmethod
    def get_facility_capabilities(self, entity_id):
        pass

    @abstractmethod
    def get_resource_capabilities(self, facility, groups):
        pass
