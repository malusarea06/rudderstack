import sys
import random
from pathlib import Path
from pytest_bdd import scenarios, given, parsers, when, then

IMPORT_PATH = Path("").absolute()
sys.path.append(str(IMPORT_PATH))

scenarios("../feature_files/scenario_one.feature")

DATA_STORE = {}

@given(parsers.parse("User should be on login page"))
def open_login_page(req, page):
    login_url = req.env_details['login_url']
    page.goto(login_url)
    print(f"Step {open_login_page.__name__} - Completed")


@given(parsers.parse("Login using username as {user_name} and password as {password}"))
def login_to_rudderstack(req, page, user_name, password):
    req.login_page.enter_username(page, user_name)
    req.login_page.enter_password(page, password)
    req.login_page.click_login(page)
    req.add_mfa.click_later_button(page)
    req.add_mfa.click_gotodash_button(page)
    req.homepage.close_tool_tip(page)
    print(f"Step {login_to_rudderstack.__name__} - Completed")


@when(parsers.parse("Navigate to connections tab under collect menu"))
def navigate_to_collect(req, page):
    req.homepage.click_collect_menu(page)
    req.homepage.click_collections_tab(page)
    print(f"Step {navigate_to_collect.__name__} - Completed")


@when("Copy the data plane url")
def step_copy_data_plane_url(req, page):
    url = req.menu_connections.get_data_plane_url(page)
    assert url, "Step failed to fetch data plane url"
    DATA_STORE['data_plane_url'] = url
    print(f"Step {step_copy_data_plane_url.__name__} - Completed")

@when("Copy the source write key")
def step_copy_source_write_key(req, page):
    key = req.menu_connections.copy_source_write_key(page)
    assert key, "Failed to fetch key"
    DATA_STORE['source_write_key'] = key
    print(f"Step {step_copy_source_write_key.__name__} - Completed")


@when("Send event to http source using api call with write_key and data_plane_url")
def step_send_event_using_api(req):
    data = req.utils.read_conf('rudder_stack.conf', 'backend_conf/')
    payload = data['identify_event']
    payload['userId'] = f'{payload['userId']}_{random.randint(0,99)}'
    auth = (DATA_STORE['source_write_key'], '')
    response = req.rudder_stack.send_identify_event(
        url=DATA_STORE['data_plane_url'], auth=auth, payload=payload
    )
    assert response.ok, "Failed to send event"
    print(f"Step {step_send_event_using_api.__name__} - Completed")


@when("Navigate to destinations tab")
def step_navigate_destinations(req, page):
    req.homepage.click_destinations_tab(page)
    print(f"Step {step_navigate_destinations.__name__} - Completed")


@when(parsers.parse("Navigate to {destination_webhook} events tab"))
def step_click_destination_hook(req, page, destination_webhook):
    req.menu_destinations.click_destinations_webhook(page, destination_webhook)
    req.menu_destinations.click_events_tab(page)
    print(f"Step {step_click_destination_hook.__name__} - Completed")


@then('Read the delivered and failed events')
def step_read_delivered_failed_events(req, page):
    delivered_events = req.menu_destinations.get_delivered_events(page)
    assert delivered_events, "Failed to validate delivered events count"
    failed_events = req.menu_destinations.get_failed_events(page)
    assert failed_events, "Failed to validate failed_event count"
    print ("Delivered Events : {}".format(delivered_events))
    print("Failed Events : {}".format(failed_events))
    print(f"Step {step_read_delivered_failed_events.__name__} - Completed")

