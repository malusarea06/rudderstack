import os
import sys
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, Playwright
from dotenv import load_dotenv, dotenv_values

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

from lib.pages.login import Login
from lib.pages.homepage import Homepage
from lib.pages.add_mfa import AddMfa


def get_env_details(env):
    load_dotenv("configs.env")
    env = env.upper()
    env_config = {
        'base_url': os.getenv(f"{env}_BASE_URL"),
        'login_url': os.getenv(f"{env}_LOGIN_URL")
    }
    return env_config

@pytest.fixture(scope="module")
def req(request):
    env = request.config.getoption('--env').lower()
    request.env_details = get_env_details(env)
    request.browser = "chromium"
    request.login_page = Login()
    request.homepage = Homepage()
    request.addmfa = AddMfa()
    yield request


@pytest.fixture(scope="module")
def page(req, playwright: Playwright):
    if req.browser == 'chromium':
        browser = playwright.chromium
    browser_ctx = browser.launch(headless=False, args=['--start-maximized'],
                                 slow_mo=1200)
    browser_ctx = browser_ctx.new_context(no_viewport=True)
    page = browser_ctx.new_page()
    yield page
    page.close()
    browser_ctx.close()
