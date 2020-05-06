"""
Abstract class PerunAdapterAbstract
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from abc import ABC


class PerunAdapterAbstract(ABC):

    LDAP = 'ldap'
    RPC = 'rpc'
