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
        # Act
        orders_line_page.click_on_first_order_of_orders_line()
        # Assert
        assert orders_line_page.wait_for_order_info_popup()

    @allure.title("Тест на проверку того, что заказы пользователя из раздела «История заказов» успешно отображаются "
                  "на странице «Лента заказов»")
    def test_orders_history_and_line(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        main_page.wait_for_downloading_disappear()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_personal_acc_button()
        private_acc_page = PrivateAccPage(login)
        private_acc_page.click_on_orders_history_link()
        # Act
        private_acc_page.scroll_to_the_last_history_order()
        history_order_number = private_acc_page.get_text_from_history_order()
        main_page = MainPage(login)
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        order_in_line = orders_line_page.get_text_from_order_line_order()
        # Assert
        assert history_order_number == order_in_line

    @allure.title("Тест на проверку того, что при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_all_time_counter(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        before = orders_line_page.get_all_time_counter()
        # Act
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        main_page.wait_for_downloading_disappear()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        orders_line_page.check_all_time_order_counter(before)
        # Assert
        after = orders_line_page.get_all_time_counter()
        assert after == before + 1

    @allure.title("Тест на проверку того, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_today_counter(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        before = orders_line_page.get_today_counter()
        # Act
        main_page.click_on_constructor_button()
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        main_page.wait_for_downloading_disappear()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        orders_line_page.check_today_order_counter(before)
        # Assert
        after = orders_line_page.get_today_counter()
        assert after == before + 1

    @allure.title("Тест на проверку того, что после оформления заказа его номер появляется в разделе В работе")
    def test_order_in_progress(self, login):
        # Arrange
        main_page = MainPage(login)
        main_page.wait_for_downloading_disappear()
        main_page.click_on_constructor_button()
        # Act
        constructor_page = ConstructorPage(login)
        constructor_page.drag_ingredient_to_order()
        constructor_page.click_on_order_button()
        order_conf_number = constructor_page.order_number_from_popup()
        main_page.wait_for_downloading_disappear()
        constructor_page.click_on_order_popup_cross()
        main_page.click_on_orders_line_button()
        orders_line_page = OrdersLinePage(login)
        in_progress_number = orders_line_page.wait_for_order_in_progress()
        # Assert
        assert order_conf_number == in_progress_number
