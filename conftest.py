from selenium import webdriver
from tests import test_num1
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(5)
    return chrome_browser
