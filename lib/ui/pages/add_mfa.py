import sys
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils import Utils

selector_conf = "addmfa.conf"

class AddMfa:
    def __init__(self):
        self.locators = Utils().read_conf(selector_conf, "pages_conf")

    def click_later_button(self, page):
        """
        __Summary__: Method to click later button on MFA screen
        :param page: current page object
        :return:
        """
        try:
            later_btn = self.locators['do_later']['value']
            page.locator(later_btn).click()
        except Exception as e:
            print("Raised exception while click on later button")

    def click_gotodash_button(self, page):
        """
        __Summary__: Method to click bashboard button on MFA screen
        :param page: current page object
        :return:
        """
        try:
            dash_btn = self.locators['goto_dash']['value']
            page.locator(dash_btn).click()
        except Exception as e:
            print("Raised exception while click on dashboard button : ",e)
