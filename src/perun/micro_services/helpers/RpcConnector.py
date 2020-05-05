import json
import logging
import pycurl
import time

from io import BytesIO

logger = logging.getLogger(__name__)


class RpcConnector:

    COOKIE_FILE = '/tmp/proxyidp_cookie.txt'
    CONNECT_TIMEOUT = 1
    TIMEOUT = 15

    rpc_url = None
    user = None
    passwd = None

    def __init__(self, rpc_url='', user='', password=''):
        self.rpc_url = rpc_url
        self.user = user
        self.passwd = password

    def post(self, manager, method, params=None):
        if params is None:
            params = []

        params_json = json.dumps(params)
        uri = "{}json/{}/{}".format(self.rpc_url, manager, method)

        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, uri)
        c.setopt(pycurl.USERPWD, self.user + ':' + self.passwd)
        c.setopt(pycurl.CUSTOMREQUEST, 'POST')
        c.setopt(pycurl.POSTFIELDS, params_json)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(pycurl.HTTPHEADER, ['Content-Type:application/json', 'Content-Length: {}'.format(len(params_json))])
        c.setopt(pycurl.CONNECTTIMEOUT, self.CONNECT_TIMEOUT)
        c.setopt(pycurl.TIMEOUT, self.TIMEOUT)

        start_time = time.time()
        c.perform()
        end_time = time.time()
        c.close()

        body = buffer.getvalue()
        # Body is a byte string.
        # We have to know the encoding in order to print it to a text file
        # such as standard output.
        result_json = body.decode('utf-8')
        result = json.loads(result_json)

        if 'errorId' in result.keys():
            raise Exception('Exception from Perun: {}'.format(result['message']))

        response_time = end_time - start_time
        logger.error(
            "POST call {} with params {}, response {} in {} ms".format(
                uri,
                params_json,
                result,
                round(response_time * 1000)
            )
        )

        return result
