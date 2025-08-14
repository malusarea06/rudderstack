# RudderStack

RudderStack is an automation framework designed to validate the UI functionality of the RudderStack web application, built using Python, Pytest, and Playwright.

## Pre-requisite
- Git [Link](https://git-scm.com/downloads)
- Python 3.13 [Link](https://www.python.org/downloads/)

## Installation
1. Clone the repo
   ```bash
    git clone https://github.com/malusarea06/rudderstack.git
   ```
2. Navigate to rudderstack folder
   ```bash
    cd rudderstack
   ```
3. Verify user is on "main" branch
   ```bash
    git branch
   ```
4. Install requirements.txt for required dependencies
   ```bash
   pip install -r requirements.txt
   ```

5. Install playwright browser dependencies
   ```bash
   playwright install
   ```



## Usage
* The framework can be executed in two-ways:
  1. Github Actions
  2. Run locally
  
## Github Actions
* The framework is integrated with CI using github actions
* The framework is executed/triggered when:
  - Changes are pushed to **main** branch.
  - Every day at 12 AM
  - Manually triggered from actions tab.

## Run locally
* To run the test suite locally, follow the above mentioned installation process.
* Use below command to run the test suite:
  ```bash
  pytest bdd_scenarios/ui_automation/step_definations/ --env=qa --browser_op=chromium --html=report.html --self-contained-html
  ```
  * Command Line Args:
    * **--env**: Environment details. Which environment to use for execution i.e (qa / prod / dev). Default is "qa".
    * **--browser_op**: Which browser to use for execution i,e  (chromium, firefox, webkit). Default is "chromium"
    * **--html**: Report name



