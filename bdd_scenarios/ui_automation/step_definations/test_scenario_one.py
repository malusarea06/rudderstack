import os
import sys
import time
from pathlib import Path
from pytest_bdd import scenarios, given, parsers, when, then

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

scenarios("../feature_files/scenario_one.feature")

@given(parsers.parse("User should be on login page"))
def test_login_page(req, page):
    login_url = req.env_details['login_url']
    page.goto(login_url)


@given(parsers.parse("Login using username as {user_name} and password as {password}"))
def login_to_rudderstack(req, page, user_name, password):
    req.login_page.enter_username(page, user_name)
    req.login_page.enter_password(page, password)
    req.login_page.click_login(page)
    req.addmfa.click_later_button(page)
    req.addmfa.click_gotodash_button(page)
    req.homepage.close_tool_tip(page)
    time.sleep(5)

@when(parsers.parse("Navigate to collect tab"))
def navigate_to_collect(req, page):
    req.homepage.click_collect_menu(page)

