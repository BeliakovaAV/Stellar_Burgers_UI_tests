import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from selenium.webdriver.common.by import By
from locators.main_functions_locators import MainFunctionsLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть на элемент")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле ввода")
    def send_keys_to_input(self, locator, keys, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_attribute(locator, attribute, value)
        )

    @allure.step('Перетащить элемент в корзину')
    def drag_and_drop_element(self, source, target):
        source_locator = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(source)
        )
        target_locator = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(target)
        )
        drag_and_drop(self.driver, source_locator, target_locator)

    @allure.step("Получить текущее значение cчетчика")
    def get_count(self, counter_locator):
        return int(self.get_text_on_element(counter_locator))


    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hide(self, locator, timeout=100):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Подождать перехода на другой url')
    def wait_for_url_change(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Найти элементы на странице')
    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    @allure.step('Найти 1 элемент на странице')
    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    @allure.step("Узнать текущий url")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Подождать, пока элемент станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Подождать, что текст элемента изменится")
    def wait_for_text_to_change(self, locator, old_text, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != old_text
        )