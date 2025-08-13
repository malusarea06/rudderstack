Feature: Feature to automate RudderStack

  Background:
    Given User should be on login page

  Scenario Outline: Send Event to Destination source
    Given Login using username as <user_name> and password as <password>
    When Copy the data plane url
    * Copy the source write key
    * Send event to http source using api call with write_key and data_plane_url
    * Navigate to destinations tab
    * Navigate to <destination_webhook> events tab
    Then Read the delivered and failed events

    Examples:
    | user_name                 | password      | destination_webhook |
    | merac34866@discrip.com    | Software@8586 | demo_http_webhook   |