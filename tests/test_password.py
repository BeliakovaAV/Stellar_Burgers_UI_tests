import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from locators.main_functions_locators import MainFunctionsLocators
from locators.password_locators import PasswordLocators
from pages.password_reset_page import PasswordResetPage
from pages.login_page import LoginPage
from pages.password_forgot_page import PasswordForgotPage
from curl import *
from data import Credentials


class TestPassword:
    @allure.title("Тест на успешный переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_recover_pass_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_personal_acc_button()
        # Act
        login_page = LoginPage(driver)
        login_page.click_on_recover_pass_link()
        # Assert
        current_url = main_page.driver.current_url
        assert current_url == forgot_password_page

    @allure.title("Тест на успешный ввод почты и клик по кнопке «Восстановить»")
    def test_email_and_recover_click(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_personal_acc_button()
        login_page = LoginPage(driver)
        login_page.click_on_recover_pass_link()
        password_forgot_page = PasswordForgotPage(driver)
        # Act
        password_forgot_page.enter_email(Credentials.email)
        password_forgot_page.click_on_recover_button()
        WebDriverWait(driver, 10).until(EC.url_to_be(reset_password_page))
        # Assert
        current_url = main_page.driver.current_url
        assert current_url == reset_password_page

    @allure.title("Тест на подсвечивание поля Пароль при клике по кнопке показать/скрыть пароль")
    def test_pass_click_light(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_personal_acc_button()
        login_page = LoginPage(driver)
        login_page.click_on_recover_pass_link()
        password_forgot_page = PasswordForgotPage(driver)
        password_forgot_page.enter_email(Credentials.email)
        password_forgot_page.click_on_recover_button()
        password_reset_page = PasswordResetPage(driver)
        password_reset_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        # Act
        password_reset_page.click_on_hide_pass_button()
        password_reset_page.wait_for_password_field_active(timeout=5)
        # Assert
        assert "active" in driver.find_element(*PasswordLocators.PASSWORD_FIELD_EYE).get_attribute("class")
