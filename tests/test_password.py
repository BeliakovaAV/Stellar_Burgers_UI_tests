import allure
import pytest

from pages.main_page import MainPage
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
        current_url = main_page.get_current_url()
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
        password_forgot_page.wait_for_url_change(reset_password_page)
        # Assert
        current_url = main_page.get_current_url()
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
        main_page.wait_for_downloading_disappear()
        # Act
        password_reset_page.click_on_hide_pass_button()
        password_reset_page.wait_for_password_field_active(timeout=5)
        # Assert
        assert password_reset_page.is_password_eye_active()
