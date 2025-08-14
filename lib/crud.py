import sys
import traceback
from pathlib import Path
import requests

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

import utils.debug_logger as debug

class CRUD:
    """
    __Summary__: Class to handle all crud operation i.e create / request / update / delete API calls
    """
    def __init__(self):
        self.debug = debug.set_debug_log(self.__class__.__name__)

    def send(self, **kwargs):
        """
        __Summary__: Method to make http call i.e get, post, put, delete
        :param kwargs:
            1. data (dict): Request payload
            2. params (dict): Query parameters
            3. headers (dict): Headers
            4. method (str): Http method
            5. url (str): Request url
            6. auth (tuple): Basic auth credentials
        :return: api_response (request)
        """
        try:
            data = kwargs.get("data", {})
            params = kwargs.get("params", {})
            headers = kwargs.get("headers", {})
            method = kwargs.get("method", '')
            url = kwargs.get("url", '')
            auth = kwargs.get("auth", '')
            if method.upper() == 'POST':
                return requests.post(url, data=data, params=params, verify=False, cookies=None,
                                     headers=headers, auth=auth)
        except requests.exceptions.RequestException as error:
            print("Exception occured while executing http call : ", error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

