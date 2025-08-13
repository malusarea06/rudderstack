import sys
from pathlib import Path
import pyperclip

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils import Utils

LOCATOR_FILE = "connections.conf"
PATH_TO_LOCATOR = "pages_conf/menu_connect"

class Connections:
    def __init__(self):
        self.locators = Utils().read_conf(LOCATOR_FILE, PATH_TO_LOCATOR)

    def get_data_plane_url(self, page):
        """
        __Summary__: Method to fetch data plane url
        :param page: Page object
        :return: data_plane_url (str)
        """
        try:
            locator = self.locators['data_plane']['value']
            page.locator(locator).click()
            data_plane_url = pyperclip.paste()
            return data_plane_url
        except Exception as e:
            print("Error while fetching the data plane url : ", e)

    def copy_source_write_key(self, page):
        """
        __Summary__: Method to copy and return the write key
        :param page: Page Object
        :return: write_key (str)
        """
        try:
            locator = self.locators['source_write_key']['value']
            page.locator(locator).click()
            write_key = pyperclip.paste()
            return write_key
        except Exception as e:
            print('Failed to return source write key : ', e)