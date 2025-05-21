import allure

from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):

    @allure.step("Кликнуть на ингредиент")
    def click_on_ingredient(self):
        self.click_on_element(MainFunctionsLocators.INGREDIENT)

    @allure.step("Кликнуть на крестик на всплывающем окне ингредиента")
    def click_on_popup_cross(self):
        self.click_on_element(MainFunctionsLocators.CROSS_ON_INGREDIENT_WINDOW)

    @allure.step('Перетащить ингредиент в заказ')
    def drag_ingredient_to_order(self):
        self.drag_and_drop(MainFunctionsLocators.INGREDIENT, MainFunctionsLocators.MOVE_INGREDIENT)

    @allure.step("Проверить, что после добавления ингредиента счётчик увеличился на 1")
    def check_ingredient_counter(self):
        before = self.get_count(MainFunctionsLocators.COUNTER)
        self.drag_ingredient_to_order(MainFunctionsLocators.INGREDIENT, MainFunctionsLocators.MOVE_INGREDIENT)
        after = self.get_count(MainFunctionsLocators.COUNTER)
        return after == before + 1

    @allure.step("Получить номер заказа из окна подтверждения") #ПОД ВОПРОСОМ
    def get_order_number(self):
        text = self.get_text_on_element(MainFunctionsLocators.ORDER_CONFIRMATION_SCREEN)
        return int(text)

