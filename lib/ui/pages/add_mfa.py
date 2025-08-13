import sys
import traceback
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils.utils import Utils
import utils.debug_logger as debug

selector_conf = "addmfa.conf"

class AddMfa:
    def __init__(self):
        self.locators = Utils().read_conf(selector_conf, "pages_conf/")
        self.debug = debug.set_debug_log(self.__class__.__name__)

    def click_later_button(self, page):
        """
        __Summary__: Method to click later button on MFA screen
        :param page: current page object
        :return:
        """
        try:
            later_btn = self.locators['do_later']['value']
            page.locator(later_btn).click()
        except Exception as error:
            print("Raised exception while click on later button")
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")

    def click_gotodash_button(self, page):
        """
        __Summary__: Method to click bashboard button on MFA screen
        :param page: current page object
        :return:
        """
        try:
            dash_btn = self.locators['goto_dash']['value']
            page.locator(dash_btn).click()
        except Exception as error:
            print("Raised exception while click on dashboard button : ",error)
            self.debug.critical(f"Exception in {debug.get_method_name()} : {traceback.format_exc()} - {error}")
