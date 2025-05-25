import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    @allure.step("Кликнуть на крестик на всплывающем окне подтверждения заказа")
    def click_on_order_popup_cross(self):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        self.wait_for_element(MainFunctionsLocators.ORDER_POPUP_CROSS)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainFunctionsLocators.ORDER_POPUP_CROSS)
        )
        self.driver.find_element(*MainFunctionsLocators.ORDER_POPUP_CROSS).click()

    @allure.step("Получить номер заказа из попапа")
    def order_number_from_popup(self):
        self.wait_for_element_hide(MainFunctionsLocators.OVERLAY)
        return self.get_text_on_element(MainFunctionsLocators.ORDER_CONFIRMATION_SCREEN)



