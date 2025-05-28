import allure
from selenium.webdriver.common.by import By

from locators.orders_line_locators import OrdersLineLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class OrdersLinePage(BasePage):

    @allure.step("Кликнуть на первый заказ в Ленте заказов")
    def click_on_first_order_of_orders_line(self):
        self.click_on_element(OrdersLineLocators.ORDER)

    @allure.step("Дождаться обновления счётчика «Выполнено за всё время»")
    def check_all_time_order_counter(self, before, increment=1, timeout=10):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        expected = str(before + increment)
        return self.wait_for_attribute(OrdersLineLocators.ALL_TIME_COUNTER, "textContent", expected, timeout)

    @allure.step("Дождаться обновления счётчика «Выполнено за сегодня»")
    def check_today_order_counter(self, before, increment=1, timeout=10):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        expected = str(before + increment)
        return self.wait_for_attribute(OrdersLineLocators.TODAY_COUNTER, "textContent", expected, timeout)

    @allure.step("Дождаться элемента в списке В работе")
    def wait_for_order_in_progress(self, timeout=15):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        locator = OrdersLineLocators.IN_PROGRESS
        old_text = self.get_text_on_element(locator)
        self.wait_for_text_to_change(locator, old_text, timeout)
        return self.get_text_on_element(locator).strip()

    @allure.step("Подождать появления попапа с информацией о заказе")
    def wait_for_order_info_popup(self):
        return self.wait_for_element(OrdersLineLocators.ORDER_POPUP_SCREEN)

    @allure.step("Получить текст с экрана заказа в ленте заказов")
    def get_text_from_order_line_order(self):
        self.get_text_on_element(OrdersLineLocators.ORDER)

    @allure.step("Получить значение счётчика За все время")
    def get_all_time_counter(self):
        return self.get_count(OrdersLineLocators.ALL_TIME_COUNTER)

    @allure.step("Получить значение счётчика За сегодня")
    def get_today_counter(self):
        return self.get_count(OrdersLineLocators.TODAY_COUNTER)