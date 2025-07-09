import allure


from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_on_personal_acc_button(self):
        self.click_on_element(MainFunctionsLocators.PERSONAL_ACC)

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element(MainFunctionsLocators.CONSTRUCTOR)

    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_on_orders_line_button(self):
        self.click_on_element(MainFunctionsLocators.ORDERS_LINE)

    @allure.step("Подождать, пока анимация загрузки пропадёт")
    def wait_for_downloading_disappear(self):
        return self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
