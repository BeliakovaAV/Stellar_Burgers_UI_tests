import allure
import pytest


from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from locators.main_functions_locators import MainFunctionsLocators
from curl import *


class TestBasicFunctions:
    @allure.title("Тест на успешный переход на страницу Конструктора по кнопке «Конструктор»")
    def test_constructor_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_personal_acc_button()
        # Act
        main_page.click_on_constructor_button()
        # Assert
        current_url = main_page.driver.current_url
        assert current_url == main_site

    @allure.title("Тест на успешный переход на страницу ленты заказов по кнопке «Лента заказов»")
    def test_orders_line_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_orders_line_button()
        # Assert
        current_url = main_page.driver.current_url
        assert current_url == orders_line_page

    @allure.title("Тест на успешное появление всплывающего окна с деталями по клику на ингредиент")
    def test_popup_ingredient(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(driver)
        # Act
        constructor_page.click_on_ingredient()
        # Assert
        assert constructor_page.wait_for_element(MainFunctionsLocators.INGREDIENT_WINDOW)

    @allure.title("Тест на успешное закрывание всплывающего окна с деталями по клику на крестик")
    def test_popup_cross(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(driver)
        constructor_page.click_on_ingredient()
        # Act
        constructor_page.click_on_popup_cross()
        # Assert
        assert constructor_page.wait_for_element_hide(MainFunctionsLocators.INGREDIENT_WINDOW)

    @allure.title("Тест на увеличение счетчика при добавлении ингредиента в заказ")
    def test_ingredient_counter(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(driver)
        # Assert
        assert constructor_page.check_ingredient_counter()

    @allure.title("Тест на успешное оформление заказа залогиненным пользователем")
    def test_order_creation(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        #Act
        constructor_page.click_on_order_button()
        # Assert
        assert constructor_page.wait_for_element(MainFunctionsLocators.ORDER_CONFIRMATION_SCREEN)

    @allure.title("Кнопка оформления заказа недоступна для неавторизованного пользователя")
    def test_make_order_button_not_visible_for_guest(self, driver):
        #Arrange
        main_page = MainPage(driver)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_constructor_button()
        # Assert
        assert not driver.find_elements(*MainFunctionsLocators.MAKE_ORDER)