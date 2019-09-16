# Web App - Automation Using Python & Selenium

This project aims to demonstrate a simple automation solution using
a page object model at it's core as a framework design.

## Tools of the trade
 * python 3.7.x
 * selenium webdriver
 * gecko driver (Firefox instance)
 * nose2 (test runner and reporter)
 * unittest (xUnit framework for implementing tests)

## Running Tests
To run the tests, you can follow the steps in order:

Move to the repo
`cd web_app`

Activate virtual env
`source venv/bin/activate`

Install package dependencies for the project
`pip install requirements.txt`

Copy `gecko driver` to python path
PATH: `/usr/local/bin`
link to firefox driver: 
`https://github.com/mozilla/geckodriver/releases`

To run all tests: 
`nose2 -v tests --html-report`

To run an individual test: 
`nose2 -v tests.test_login_flow --html-report`

To deactivate virtualenv
`deactivate`

## Viewing Reports
You can view reports at: `/reports` within the repo. The reports are
in HTML format and can be viewed in any browser of choice.

## Design Decisions
The overall design of the web app automation code follows the principle
of Page Object Model. 
The tests call on action methods which in turn use element locators
to do specific tasks of replicating user behaviour.

The project code is split across multiple package (or folders), each
segregated to better isolate their functioning. 

The core folders are listed below with a brief summary:

 * `element_locators`: This package is for storing element locators which
 are separated based on the pages the elements are present in.
 * `pages`: This package is for storing action methods which can be
 performed on the elements in a particular page.
 * `report`: This package stores the last run report in HTML format.
 * `screenshots`: This package can store screenshots which can come
 in handy when trying to go over the automation runs.
 * `test_data`: This package can be used to store relevant test data
 or information which can be used across multiple tests.
 * `test`: This package holds all the tests. Each test script can hold
 a set of tests, mostly grouped by page level actions.
 * `venv`: This is the virtual environment set up package. The isolated
 python packages (3rd party python packages) are set up here. This 
 ensures the entire code repo has only project specific packages which
 do not impact system wide packages thereby creating a good buffer of
 need based packages per project.
 * Additional Files:
    * `nose2.cfg`: This config file allows us to set up nose2 cmd line
    runner. It let's us export reports in HTML format.
    * `requirements.txt`: It keeps a simple copy of external python 
    packages or dependencies required to run the tests. It works well
    with `pip`, the python package manager to setup the dependencies.
    
    
## Additional Design Decisions:

While it was tempting to create a base page within the pages folder
and make all other classes to inherit from this file, I've tried to 
limit the amount of inheritance across the project. Judicial use of
composition is favoured over this. The only case of inheritance can 
be seen across the test scripts which allow use to remove writing the
`setUp` and `tearDown` methods in each script advocating a better case
of DRY code usage.

Also, another decision was to store the `gecko driver` within the python
path instead of adding it to the repo to avoid bulking up the size of
the repo. 

Future improvements to this particular code can come in the form of
removing test data and using factory methods to generate data seeding.

Also, as the project can grow in tests and scale, we can incorporate
a steady mix of cross-browser testing by adding a chrome driver and
internet explorer driver to ensure we cover more relatable user flows
and real world scenario emulation.
