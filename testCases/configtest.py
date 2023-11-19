import pytest
from selenium import webdriver


def setup():
    driver = webdriver.Chrome()
    return driver

# @pytest.fixture
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching chrome browser............")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching firefox browser............")
#
#     else:
#         driver = webdriver.Ie()
#
#     return driver
#
#
# def pytest_adoption(parser):  # this will get the value from CLI/hooks
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):  # this will return the browser value to setup method
#     return request.config.getoption("--browser")


############################# Pytest HTML Reports##################33
