import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from locators.private_acc_locators import PrivateAccLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class PrivateAccPage(BasePage):

    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_on_orders_history_link(self):
        self.click_on_element(PrivateAccLocators.HISTORY_LINK)

    @allure.step("Кликнуть на ссылку 'Выход'")
    def click_on_exit_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainFunctionsLocators.OVERLAY)
        )
        exit_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PrivateAccLocators.EXIT_LINK)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true); arguments[0].click();",
            exit_link
        )
