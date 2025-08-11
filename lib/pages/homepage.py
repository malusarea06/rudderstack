import sys
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils import Utils

selector_conf = "homepage.conf"

class Homepage:
    def __init__(self):
        self.locators = Utils().read_conf(selector_conf, "pages_conf")

    def click_collect_menu(self, page):
        """
        Summary: Method to select collect menu
        :param page: current page object
        :return:
        """
        try:
            collect_menu = self.locators['menu_sidebar']['collect_menu']['value']
            page.locator(collect_menu).click()
        except Exception as e:
            print("Failed to click collect menu", e)

    def close_tool_tip(self, page):
        """
        Summary: Method to clos the tool tip dailog
        :param page: current page object
        :return:
        """
        try:
            close_loc = self.locators['tooltip']['close_tip']['value']
            page.locator(close_loc).click()
        except Exception as e:
            print("Failed to click close tip")
