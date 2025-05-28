import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.private_acc_page import PrivateAccPage
from locators.main_functions_locators import MainFunctionsLocators
from curl import *
from data import Credentials


class TestPrivateAcc:
    @allure.title("Тест на успешный переход на страницу Личного кабинета по кнопке «Личный кабинет»")
    def test_recover_pass_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_personal_acc_button()
        # Assert
        current_url = main_page.get_current_url()
        assert current_url == login_page

    @allure.title("Тест на успешный переход на страницу Истории заказов")
    def test_orders_history(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_personal_acc_button()
        private_acc_page = PrivateAccPage(login)
        # Act
        private_acc_page.click_on_orders_history_link()
        # Assert
        assert login.current_url == history_page

    @allure.title("Тест на успешный выход из аккаунта")
    def test_acc_exit(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_personal_acc_button()
        private_acc_page = PrivateAccPage(login)
        # Act
        private_acc_page.click_on_exit_link()
        private_acc_page.wait_for_url_change(login_page)
        # Assert
        assert login.current_url == login_page