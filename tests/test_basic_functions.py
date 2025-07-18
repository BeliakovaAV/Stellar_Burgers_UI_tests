import allure
import pytest


from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
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
        current_url = main_page.get_current_url()
        assert current_url == main_site

    @allure.title("Тест на успешный переход на страницу ленты заказов по кнопке «Лента заказов»")
    def test_orders_line_button(self, driver):
        # Arrange
        main_page = MainPage(driver)
        # Act
        main_page.click_on_orders_line_button()
        # Assert
        current_url = main_page.get_current_url()
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
        assert constructor_page.wait_for_ingredient_popup_appear()

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
        assert constructor_page.wait_for_ingredient_popup_disappear()

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
        main_page.wait_for_downloading_disappear()
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        #Act
        constructor_page.click_on_order_button()
        # Assert
        assert constructor_page.wait_for_order_confirmation_popup_appear()

    @allure.title("Кнопка оформления заказа недоступна для неавторизованного пользователя")
    def test_make_order_button_not_visible_for_guest(self, driver):
        #Arrange
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(driver)
        # Assert
        assert not constructor_page.find_order_button()