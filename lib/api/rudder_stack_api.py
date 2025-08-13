import json
import sys
import traceback
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from lib.crud import CRUD
import utils.debug_logger as debug

ENDPOINTS = {
    "identify": {"endpoint": "/v1/identify", "method": "post"}
}

class RudderStackAPI:
    """
    __Summary__: Method to handle rudder stack http api calls
    """

    def __init__(self):
        self.crud = CRUD()
        self.debug = debug.set_debug_log(self.__class__.__name__)

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
        except Exception as error:
            print("Raised exception while send identify event : ", error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")