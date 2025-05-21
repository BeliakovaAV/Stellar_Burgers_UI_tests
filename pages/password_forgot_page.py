import allure

from locators.password_locators import PasswordLocators
from pages.base_page import BasePage


class PasswordForgotPage(BasePage):

    @allure.step("Ввести почту в поле 'Email'")
    def enter_email(self, email):
        self.click_on_element(PasswordLocators.EMAIL_FIELD_PASS)
        self.send_keys_to_input(PasswordLocators.EMAIL_FIELD_PASS, email)

    @allure.step("Кликнуть на кнопку 'Восстановить'")
    def click_on_recover_button(self):
        self.click_on_element(PasswordLocators.RECOVER_PASS_BUTTON)