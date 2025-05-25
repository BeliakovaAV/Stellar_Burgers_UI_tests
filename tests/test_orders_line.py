import allure
import pytest

from pages.main_page import MainPage
from pages.orders_line_page import OrdersLinePage
from locators.orders_line_locators import OrdersLineLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.private_acc_page import PrivateAccPage
from pages.constructor_page import ConstructorPage


class TestOrdersLine:
    @allure.title("Тест на успешное появление всплывающего окна с деталями по клику на заказ")
    def test_popup_order(self, driver):
        # Arrange
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(driver)
        order_number = orders_line_page.get_text_on_element(OrdersLineLocators.ORDER)
        # Act
        orders_line_page.click_on_first_order_of_orders_line()
        # Assert
        popup_locator = orders_line_page.order_popup_locator(order_number)
        assert orders_line_page.wait_for_element(popup_locator)

    @allure.title("Тест на проверку того, что заказы пользователя из раздела «История заказов» успешно отображаются "
                  "на странице «Лента заказов»")
    def test_orders_history_and_line(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_personal_acc_button()
        private_acc_page = PrivateAccPage(login)
        private_acc_page.click_on_orders_history_link()
        # Act
        private_acc_page.scroll_to_element(OrdersLineLocators.ORDER_HISTORY_SCREEN)
        history_order_number = private_acc_page.get_text_on_element(OrdersLineLocators.ORDER_HISTORY_SCREEN)
        main_page = MainPage(login)
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        line_order_number = orders_line_page.get_text_on_element(OrdersLineLocators.ORDER)
        # Assert
        assert history_order_number == line_order_number

    @allure.title("Тест на проверку того, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_all_time_counter(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        before = orders_line_page.get_count(OrdersLineLocators.ALL_TIME_COUNTER)
        # Act
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        orders_line_page.check_all_time_order_counter(before)
        # Assert
        after = orders_line_page.get_count(OrdersLineLocators.ALL_TIME_COUNTER)
        assert after == before + 1

    @allure.title("Тест на проверку того, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_counter(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        before = orders_line_page.get_count(OrdersLineLocators.TODAY_COUNTER)
        # Act
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        orders_line_page.check_today_order_counter(before)
        # Assert
        after = orders_line_page.get_count(OrdersLineLocators.TODAY_COUNTER)
        assert after == before + 1

    @allure.title("Тест на проверку того, что после оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        main_page.click_on_constructor_button()
        # Act
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        order_conf_number = constructor_page.order_number_from_popup()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        in_progress_number = orders_line_page.wait_for_order_in_progress()
        # Assert
        assert order_conf_number == in_progress_number
