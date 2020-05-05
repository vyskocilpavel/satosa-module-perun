"""
Satosa micro_service : Perun Entitlement
"""

__author__ = "Pavel Vyskocil"
__email__ = "Pavel.Vyskocil@cesnet.cz"

import logging
from typing import List

from perun.micro_services.helpers.PerunAdapter import PerunAdapter
from perun.micro_services.helpers.PerunAdapterAbstract import PerunAdapterAbstract
from perun.micro_services.models.Facility import Facility
from perun.micro_services.models.Group import Group

from satosa.micro_services.base import ResponseMicroService


logger = logging.getLogger(__name__)


class PerunEntitlement(ResponseMicroService):
    INTERFACE = 'interface'
    PREFIX = 'prefix'
    SUFFIX = 'suffix'
    PERUN_CONFIG_FILE_NAME = 'perun_config_file_name'

    def __init__(self, config, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.config = config

        if not config[self.PERUN_CONFIG_FILE_NAME]:
            raise Exception(f'PerunIdentity: Required option "{self.PERUN_CONFIG_FILE_NAME}" not defined.')

        interface = str.lower(config.get(self.INTERFACE))
        self.adapter: PerunAdapterAbstract = PerunAdapter.get_instance(config[self.PERUN_CONFIG_FILE_NAME], interface)

        self.prefix = config.get(self.PREFIX, '')
        self.suffix = config.get(self.SUFFIX, '')

    def process(self, context, data):
        sp_entity_id = data.requester
        facility = self.adapter.get_facility_by_entity_id(sp_entity_id)
        user_id = data.attributes['perun_id'][0]

        groups = self.adapter.get_user_groups_on_facility(user_id, facility)

        group_names = []

        for group in groups:
            group_names.append(self.__groupname_wrapper(group.name))

        capabilities = self.__get_capabilities(facility, groups)

        entitlements = capabilities + group_names
        data.attributes.update({'edupersonentitlement': entitlements})

        return super().process(context, data)

    def __get_capabilities(self, facility: Facility, groups: List[Group]):
        """
        Get capabilities

        :param facility: Facility object
        :param groups: List of Groups
        :return: returns List of strings
        """
        resource_capabilities = []
        facility_capabilities = []

        try:
            resource_capabilities = self.adapter.get_resource_capabilities(facility, groups)
            facility_capabilities = self.adapter.get_facility_capabilities(facility.id)
        except Exception:
            logger.error('Exception during get Capability')

        capabilities = []
        for capability in (resource_capabilities + facility_capabilities):
            capabilities.append(self.__capabilities_wrapper(capability))

        return capabilities

    def __capabilities_wrapper(self, name):
        """
        Wrap name with the prefix and suffix to the correct form.

        :param name: The capability string
        :return: Returns string
        """
        return f'{self.prefix}:{name}#{self.suffix}'

    def __groupname_wrapper(self, name):
        """
        Wrap name with the prefix and suffix to the correct form.
        TODO: Group should be url encoded.

        :param name: The capability string
        :return: Returns string
        """
        return f'{self.prefix}:group:{name}#{self.suffix}'
