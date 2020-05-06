import logging

import yaml
from perun.micro_services.adapters.PerunAdapterAbstract import PerunAdapterAbstract
from perun.micro_services.adapters.RpcConnector import RpcConnector
from perun.micro_services.models.User import User

logger = logging.getLogger(__name__)


class RpcAdapter(PerunAdapterAbstract):

    PERUN_CONFIG_FILE_NAME = 'perun_config_file_name'

    PERUN_RPC_HOSTNAME = 'rpc.hostname'
    PERUN_RPC_USER = 'rpc.user'
    PERUN_RPC_PASSWORD = 'rpc.password'

    connector = None

    def __init__(self, config_file):

        with open(config_file, "r") as f:
            perun_configuration = yaml.safe_load(f)
            hostname = perun_configuration.get(self.PERUN_RPC_HOSTNAME, None)
            user = perun_configuration.get(self.PERUN_RPC_USER, None)
            pasword = perun_configuration.get(self.PERUN_RPC_PASSWORD, None)

        if None in [hostname, user, pasword]:
            raise Exception('One of required attributes is not defined!')

        self.connector = RpcConnector(hostname, user, pasword)

    def get_perun_user(self, idp_entity_id, uids):
        user = None

        for uid in uids:
            try:
                result = self.connector.get('usersManager', 'getUserByExtSourceNameAndExtLogin', {
                    'extSourceName': idp_entity_id,
                    'extLogin': uid
                })

                name = ''
                for item in ['titleBefore', 'firstName', 'middleName', 'lastName', 'titleAfter']:
                    field = result[item]

                    if field is not None and field.strip():
                        name += field + ' '

                name = name.strip()
                logger.debug("User is found")
                return User(result['id'], name)
            except Exception as ex:
                logger.debug(ex.args)

        logger.debug('User not found')
        return user
