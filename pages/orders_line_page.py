import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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

    @allure.step("Найти и прокрутить к номеру заказа в ленте")
    def find_order_in_feed(self, order_number: str, timeout: int = 10) -> bool:
        container = self.driver.find_element(*OrdersLineLocators.ORDERS_LIST_CONTAINER)
        end_time = time.time() + timeout
        last_height = -1

        while time.time() < end_time:
            try:
                elem = container.find_element(*OrdersLineLocators.ORDER_NUMBER_IN_LIST(order_number))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
                return True
            except NoSuchElementException:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", container)
                time.sleep(0.5)
                new_height = self.driver.execute_script("return arguments[0].scrollHeight;", container)
                if new_height == last_height:
                    break
                last_height = new_height

        return False