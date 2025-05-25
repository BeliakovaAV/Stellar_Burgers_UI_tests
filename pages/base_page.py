import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
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

    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_on_order_button(self):
        self.click_on_element(MainFunctionsLocators.MAKE_ORDER)

    @allure.step('Подождать пока элемент станет невидимым')
    def wait_for_element_hide(self, locator, timeout=100):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

