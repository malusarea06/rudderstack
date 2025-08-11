Feature: Feature to automate RudderStack

  Background:
    Given User should be on login page

  Scenario Outline: Send Event to Destination source
    Given Login using username as <user_name> and password as <password>
    When Navigate to collect tab

    Examples:
    | user_name                 | password      |
    | merac34866@discrip.com    | Software@8586 |