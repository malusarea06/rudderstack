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
        later_btn = self.locators['do_later']['value']
        page.locator(later_btn).click()

    def click_gotodash_button(self, page):
        dashb_btn = self.locators['goto_dash']['value']
        page.locator(dashb_btn).click()
        # page.keyboard.press('Escape')