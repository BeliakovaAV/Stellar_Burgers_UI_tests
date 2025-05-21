import allure

from locators.password_locators import PasswordLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_on_recover_pass_link(self):
        self.click_on_element(PasswordLocators.RESET_PASS_LINK)

