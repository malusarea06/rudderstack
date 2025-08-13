import sys
import traceback
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils.utils import Utils
import utils.debug_logger as debug

LOCATOR_FILE = "destinations.conf"
PATH_TO_LOCATOR = "pages_conf/menu_connect"

class Destinations:
    def __init__(self):
        self.locators = Utils().read_conf(LOCATOR_FILE, PATH_TO_LOCATOR)
        self.debug = debug.set_debug_log(self.__class__.__name__)


    def click_destinations_webhook(self, page, destination_webhook):
        """
        __Summary__: Method to select destinations webhook
        :return:
        """
        try:
            dest_locator = self.locators['destination_webhook']['value'].replace('webhook', destination_webhook)
            page.locator(dest_locator).click()
        except Exception as error:
            print("Error while selecting destination webhook : ", error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

    def click_events_tab(self, page):
        """
        __Summary__: Method to click destinations events tab
        :param page: Page object
        :return:
        """
        try:
            event_loc = self.locators['events_tab']['value']
            page.locator(event_loc).click()
        except Exception as error:
            print("Error while clicking on events tab")
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

    def get_delivered_events(self, page):
        """
        __Summary__: Method to fetch or read delivered events
        :param page: page object
        :return: delivered_events (str)
        """
        try:
            delv_events = self.locators['delivered_events']['value']
            delivered_events = page.locator(delv_events).text_content()
            if delivered_events:
                return delivered_events
            return None
        except Exception as error:
            print('Failed to fetch the delivered count')
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

    def get_failed_events(self, page):
        """
        __Summary__: Method to fetch or read failed events
        :param page: page object
        :return: failed_events (str)
        """
        try:
            fail_events = self.locators['failed_events']['value']
            failed_events = page.locator(fail_events).text_content()
            if failed_events:
                return failed_events
            return None
        except Exception as error:
            print('Failed to fetch the failed count')
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")