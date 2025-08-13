import os
import sys
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from lib.ui.pages.login import Login
from lib.ui.pages.homepage import Homepage
from lib.ui.pages.add_mfa import AddMfa
from lib.ui.pages.menu_connect.connections import Connections
from lib.ui.pages.menu_connect.destinations import Destinations
from lib.api.rudder_stack_api import RudderStackAPI
from utils.utils import Utils


def get_env_details(env):
    load_dotenv("configs.env")
    env = env.upper()
    env_config = {
        'base_url': os.getenv(f"{env}_BASE_URL"),
        'login_url': os.getenv(f"{env}_LOGIN_URL"),
        'username': os.getenv(f"{env}_USER_EMAIL"),
        'password': os.getenv(f"{env}_USER_PASSWORD")
    }
    return env_config

@pytest.fixture(scope="module")
def req(request):
    env = request.config.getoption('--env').lower()
    request.browsr = request.config.getoption('--browser_op').lower()
    request.env_details = get_env_details(env)
    request.login_page = Login()
    request.homepage = Homepage()
    request.add_mfa = AddMfa()
    request.rudder_stack = RudderStackAPI()
    request.menu_connections = Connections()
    request.menu_destinations = Destinations()
    request.utils = Utils()
    yield request


@pytest.fixture(scope="module")
def page(req):
    playwright = sync_playwright().start()
    if req.browsr == 'chromium':
        browser = playwright.chromium
    if req.browsr == 'firefox':
        browser = playwright.firefox
    browser_ctx = browser.launch(headless=False, args=['--start-maximized'],
                                 slow_mo=1100)
    browser_ctx = browser_ctx.new_context(no_viewport=True)
    page = browser_ctx.new_page()
    yield page
    browser_ctx.close()
    playwright.stop()
