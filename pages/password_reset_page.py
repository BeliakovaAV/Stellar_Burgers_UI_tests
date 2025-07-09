import allure

from locators.password_locators import PasswordLocators
from pages.base_page import BasePage


class PasswordResetPage(BasePage):
    @allure.step("Кликнуть по кнопке показать/скрыть пароль")
    def click_on_hide_pass_button(self):
        self.click_on_element(PasswordLocators.EYE_ICON)

    @allure.step("Подождать, пока поле Пароль не получит статус active")
    def wait_for_password_field_active(self, timeout=10):
        return self.wait_for_attribute(PasswordLocators.PASSWORD_FIELD_EYE, "class", "active", timeout)

    @allure.step("Проверить, что иконка видимости пароля активна")
    def is_password_eye_active(self):
        element = self.find_element(*PasswordLocators.PASSWORD_FIELD_EYE)
        return "active" in element.get_attribute("class")