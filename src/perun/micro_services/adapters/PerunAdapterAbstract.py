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
