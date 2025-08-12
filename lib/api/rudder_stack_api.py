import json
import sys
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from lib.crud import CRUD

ENDPOINTS = {
    "identify": {"endpoint": "/v1/identify", "method": "post"}
}

class RudderStackAPI:
    """
    __Summary__: Method to handle rudder stack http api calls
    """

    def __init__(self):
        self.crud = CRUD()

    def send_identify_event(self, **kwargs):
        """
        __Summary__ : Method to call identify event api
        :param kwargs:
            1. auth (tuple): Basic auth credentials
            2. payload (dict): Request payload
            3. url (str): Base Url
        :return:
        """
        try:
            auth = kwargs.get('auth', ())
            payload = kwargs.get('payload', {})
            url = kwargs.get('url')
            headers = {'Content-Type': 'application/json'}
            url = url + ENDPOINTS['identify']['endpoint']
            method = ENDPOINTS['identify']['method']
            api_response = self.crud.send(url=url, auth=auth, data=json.dumps(payload), headers=headers, method=method)
            return api_response
        except Exception as e:
            print("Failed to send identify event : ", e)