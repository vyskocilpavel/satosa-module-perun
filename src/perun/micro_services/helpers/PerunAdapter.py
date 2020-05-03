from abc import ABC, abstractmethod


class PerunAdapter(ABC):

    LDAP = 'ldap'
    RPC = 'rpc'

    @abstractmethod
    def get_perun_user(self, idp_entity_id, uids):
        pass
