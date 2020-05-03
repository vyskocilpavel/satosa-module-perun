"""
SATOSA microservice that outputs log in custom format.
"""

import logging

from perun.micro_services.helpers.LdapAdapter import LdapAdapter
from perun.micro_services.helpers.PerunAdapter import PerunAdapter
from perun.micro_services.helpers.RpcAdapter import RpcAdapter

from satosa.micro_services.base import ResponseMicroService


logger = logging.getLogger(__name__)


class PerunIdentity(ResponseMicroService):
    """
    Use context and data object to create custom log output
    """
    INTERFACE = 'interface'
    UIDS_IDENTIFIERS = 'uids_identifiers'

    logprefix = "PerunIdentity:"
    adapter = None
    uids_identifiers = None

    def __init__(self, config, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.config = config

        self.uids_identifiers = config.get(self.UIDS_IDENTIFIERS, [])
        interface = 'rpc'
        if config[self.INTERFACE]:
            interface = str.lower(config.get(self.INTERFACE, 'rpc'))

        if interface == PerunAdapter.LDAP:
            self.adapter = LdapAdapter(config)
        else:
            self.adapter = RpcAdapter(config)

    def process(self, context, data):
        idp_entity_id = data.auth_info['issuer']
        attributes = data.attributes

        uids = []

        for identifier in self.uids_identifiers:
            if identifier in attributes.keys():
                uid = attributes[identifier][0]
                uids.append(uid)

        user = self.adapter.get_perun_user(idp_entity_id, uids)

        logger.error(f"User: {user} found")
        if user is not None:
            attributes.update({'perun_id': [user.getId()]})
            data.attributes = attributes

        return super().process(context, data)
