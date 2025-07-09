import allure

from locators.private_acc_locators import PrivateAccLocators
from locators.orders_line_locators import OrdersLineLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class PrivateAccPage(BasePage):

    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_on_orders_history_link(self):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        self.scroll_to_element(PrivateAccLocators.HISTORY_LINK)
        self.click_on_element(PrivateAccLocators.HISTORY_LINK)

    @allure.step("Кликнуть на ссылку 'Выход'")
    def click_on_exit_link(self):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        self.scroll_to_element(PrivateAccLocators.EXIT_LINK)
        self.wait_for_element_to_be_clickable(PrivateAccLocators.EXIT_LINK)
        self.click_on_element(PrivateAccLocators.EXIT_LINK)

    @allure.step("Проскроллить до самого нижнего заказа в истории заказов")
    def scroll_to_the_last_history_order(self):
        self.scroll_to_element(OrdersLineLocators.ORDER_HISTORY_SCREEN)

    @allure.step("Получить текст с экрана заказа")
    def get_text_from_history_order(self):
        self.get_text_on_element(OrdersLineLocators.ORDER_HISTORY_SCREEN)

    @allure.step("Выполнить вход в личный кабинет")
    def login(self, email, password):
        self.find_element(*PrivateAccLocators.PERSONAL_ACC).click()
        self.find_element(*PrivateAccLocators.ACC_EMAIL).send_keys(email)
        self.find_element(*PrivateAccLocators.ACC_PASSWORD).send_keys(password)
        self.find_element(*PrivateAccLocators.ENTER).click()