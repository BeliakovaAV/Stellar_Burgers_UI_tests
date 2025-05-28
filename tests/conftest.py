import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from curl import *
from data import Credentials
from pages.private_acc_page import PrivateAccPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(main_site)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    private_acc_page = PrivateAccPage(driver)
    private_acc_page.login(Credentials.email, Credentials.password)
    return driver
