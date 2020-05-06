import logging

import yaml
from perun.micro_services.adapters.PerunAdapterAbstract import PerunAdapterAbstract
from perun.micro_services.adapters.RpcConnector import RpcConnector

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
