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
        self.drag_and_drop_element(MainFunctionsLocators.INGREDIENT, MainFunctionsLocators.MOVE_INGREDIENT)

    @allure.step("Проверить, что после добавления ингредиента счётчик увеличился на 1")
    def check_ingredient_counter(self):
        before = self.get_count(MainFunctionsLocators.COUNTER)
        self.drag_ingredient_to_order()
        expected = before + 2
        self.wait_for_attribute(MainFunctionsLocators.COUNTER, "textContent", str(expected))
        after = self.get_count(MainFunctionsLocators.COUNTER)
        return after == expected

    @allure.step("Кликнуть на кнопку Оформить заказ")
    def click_on_make_order(self):
        self.click_on_element(MainFunctionsLocators.MAKE_ORDER)


    @allure.step("Получить номер заказа из окна подтверждения") #ПОД ВОПРОСОМ
    def get_order_number(self):
        text = self.get_text_on_element(MainFunctionsLocators.ORDER_CONFIRMATION_SCREEN)
        return int(text)

