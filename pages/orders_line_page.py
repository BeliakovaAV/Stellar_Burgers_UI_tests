import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

from locators.orders_line_locators import OrdersLineLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class OrdersLinePage(BasePage):

    @allure.step("Кликнуть на первый заказ в Ленте заказов")
    def click_on_first_order_of_orders_line(self):
        self.click_on_element(OrdersLineLocators.ORDER)

    @allure.step("Сформировать локатор номера заказа в попапе")
    def order_popup_locator(self, order_number):
        return By.XPATH, f"//div[contains(@class,'Modal')]//p[text()='{order_number}']"

    @allure.step("Дождаться обновления счётчика «Выполнено за всё время»")
    def check_all_time_order_counter(self, before, increment=1, timeout=10):
        expected = str(before + increment)
        return self.wait_for_attribute(OrdersLineLocators.ALL_TIME_COUNTER, "textContent", expected, timeout)

    @allure.step("Дождаться обновления счётчика «Выполнено за сегодня»")
    def check_today_order_counter(self, before, increment=1, timeout=10):
        expected = str(before + increment)
        return self.wait_for_attribute(OrdersLineLocators.TODAY_COUNTER, "textContent", expected, timeout)

    @allure.step("Дождаться элемента в списке В работе")
    def wait_for_order_in_progress(self, timeout=15):
        locator = OrdersLineLocators.IN_PROGRESS
        old_text = self.get_text_on_element(locator)
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != old_text
        )
        return self.get_text_on_element(locator).strip()

