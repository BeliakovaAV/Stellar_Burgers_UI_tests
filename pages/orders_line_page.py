import allure

from locators.order_line_locators import OrdersLineLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class OrdersLinePage(BasePage):

    @allure.step("Кликнуть на первый заказ в Ленте заказов")
    def click_on_first_order_of_orders_line(self):
        self.click_on_element(OrdersLineLocators.ORDER)

    @allure.step("Проверить, что заказ с номером {order_number} отображается в Ленте заказов")  # ПОД ВОПРОСОМ
    def is_order_in_orders_line(self):
        self.wait_for_element(OrdersLineLocators.ORDER_LINE_SCREEN)

    @allure.step("Проверить, что после добавления заказа счётчик за все время увеличился на 1")
    def check_all_time_order_counter(self):
        before = self.get_count(OrdersLineLocators.ALL_TIME_COUNTER)
        self.click_on_order_button(MainFunctionsLocators.MAKE_ORDER)
        after = self.get_count(OrdersLineLocators.ALL_TIME_COUNTER)
        return after == before + 1

    @allure.step("Проверить, что после добавления заказа счётчик за сегодня увеличился на 1")
    def check_today_order_counter(self):
        before = self.get_count(OrdersLineLocators.TODAY_COUNTER)
        self.click_on_order_button(MainFunctionsLocators.MAKE_ORDER)
        after = self.get_count(OrdersLineLocators.TODAY_COUNTER)
        return after == before + 1

    @allure.step("Проверить, что заказ {order_number} отображается в разделе 'В работе'") #ПОД ВОПРОСОМ
    def is_order_in_progress(self):
        self.wait_for_element(OrdersLineLocators.IN_PROGRESS_COUNTER)