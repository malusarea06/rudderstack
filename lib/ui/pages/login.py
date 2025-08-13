import sys
from pathlib import Path

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from utils import Utils

selector_conf = "login.conf"

class Login:
    def __init__(self):
        self.locators = Utils().read_conf(selector_conf, "pages_conf")

    def enter_username(self, page, user_name):
        """
        Method to enter user name on login page
        :param page: current page object
        :param user_name: User name for login
        :return: True/False
        """
        try:
            input_loc = self.locators['user_name']['value']
            page.get_by_test_id(input_loc).fill(user_name)

        except Exception as e:
            print("Raised exception while enter user name : ", e)

    def enter_password(self, page, user_name):
        """
        Method to enter password on login page
        :param page: current page object
        :param user_name: Password for login
        :return: True/False
        """
        try:
            input_loc = self.locators['password']['value']
            page.get_by_test_id(input_loc).fill(user_name)
        except Exception as e:
            print("Raised exception while enter password : ", e)

    def click_login(self, page):
        """
        Method to perform click action on login button
        :param page: current page object
        :return:
        """
        try:
            login_btn = self.locators['login_btn']['value']
            page.locator(login_btn).click()
        except Exception as e:
            print("Raised exception while click login button")