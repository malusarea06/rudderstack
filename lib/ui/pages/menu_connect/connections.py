import sys
import traceback
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils.utils import Utils
import utils.debug_logger as debug

LOCATOR_FILE = "connections.conf"
PATH_TO_LOCATOR = "pages_conf/menu_connect"

class Connections:
    def __init__(self):
        self.locators = Utils().read_conf(LOCATOR_FILE, PATH_TO_LOCATOR)
        self.debug = debug.set_debug_log(self.__class__.__name__)

    def get_data_plane_url(self, page):
        """
        __Summary__: Method to fetch data plane url
        :param page: Page object
        :return: data_plane_url (str)
        """
        try:
            locator = self.locators['data_plane']['value']
            data_plane_url = page.locator(locator).text_content()
            return data_plane_url
        except Exception as error:
            print("Error while fetching the data plane url : ", error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

    def copy_source_write_key(self, page):
        """
        __Summary__: Method to copy and return the write key
        :param page: Page Object
        :return: write_key (str)
        """
        try:
            locator = self.locators['source_write_key']['value']
            write_key = page.locator(locator).text_content()
            write_key = write_key.split(" ")[-1]
            return write_key
        except Exception as error:
            print('Failed to return source write key : ', error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")