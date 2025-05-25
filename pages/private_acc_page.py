import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators.private_acc_locators import PrivateAccLocators
from locators.main_functions_locators import MainFunctionsLocators
from pages.base_page import BasePage


class PrivateAccPage(BasePage):

    @allure.step("Кликнуть на ссылку 'История заказов'")
    def click_on_orders_history_link(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainFunctionsLocators.OVERLAY)
        )
        history_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PrivateAccLocators.HISTORY_LINK)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true); arguments[0].click();",
            history_link
        )

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
