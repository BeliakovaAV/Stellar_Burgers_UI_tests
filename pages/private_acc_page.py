import allure

from locators.private_acc_locators import PrivateAccLocators
from pages.base_page import BasePage


class PrivateAccPage(BasePage):

    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_on_orders_history_link(self):
        self.click_on_element(PrivateAccLocators.HISTORY_LINK)

    @allure.step("Кликнуть на ссылку 'Выход'")
    def click_on_exit_link(self):
        self.click_on_element(PrivateAccLocators.EXIT_LINK)