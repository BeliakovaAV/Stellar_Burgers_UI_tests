import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from curl import *
from data import Credentials
from locators.private_acc_locators import PrivateAccLocators


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
    driver.find_element(*PrivateAccLocators.PERSONAL_ACC).click()
    driver.find_element(*PrivateAccLocators.ACC_EMAIL).send_keys(Credentials.email)
    driver.find_element(*PrivateAccLocators.ACC_PASSWORD).send_keys(Credentials.password)
    driver.find_element(*PrivateAccLocators.ENTER).click()

    return driver





