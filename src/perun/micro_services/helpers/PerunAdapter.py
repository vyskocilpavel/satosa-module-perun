"""
Class PerunAdapter
"""
__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

from perun.micro_services.helpers.LdapAdapter import LdapAdapter
from perun.micro_services.helpers.PerunAdapterAbstract import PerunAdapterAbstract
from perun.micro_services.helpers.RpcAdapter import RpcAdapter


class PerunAdapter:

    @staticmethod
    def get_instance(config_file_path, interface=PerunAdapterAbstract.RPC):
        if interface == PerunAdapterAbstract.LDAP:
            adapter = LdapAdapter(config_file_path)
        else:
            adapter = RpcAdapter(config_file_path)
        return adapter
