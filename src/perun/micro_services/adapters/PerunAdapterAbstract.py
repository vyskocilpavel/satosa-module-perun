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
    def get_facility_by_identifier(self, identifier):
        pass

    @abstractmethod
    def get_user_groups_on_facility(self, user, facility_id):
        pass

    @abstractmethod
    def get_facility_capabilities(self, facility_id):
        pass

    @abstractmethod
    def get_resource_capabilities(self, facility_id, groups):
        pass

    @abstractmethod
    def get_user_attributes_values(self, user_id, attributes):
        pass
