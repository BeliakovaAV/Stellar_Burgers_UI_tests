from selenium.webdriver.common.by import By


class OrdersLineLocators:
    ORDER = [By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]//p[contains(@class, 'text_type_digits-default')]"] # первый заказ  в ленте"
    ORDER_HISTORY_SCREEN = [By.XPATH, "//ul[contains(@class, 'OrderHistory_list')]/li[last()]//p[contains(@class, "
                                      "'text_type_digits-default')]"] #заказ со страницы Истории Заказов
    ALL_TIME_COUNTER = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] # счетчик за все время
    TODAY_COUNTER = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] # счетчик за сегодня
    IN_PROGRESS = (By.CSS_SELECTOR, "ul[class*='OrderFeed_orderListReady'] > li") # первое значение в списке В работе
    ORDER_POPUP_SCREEN = (By.CSS_SELECTOR, "section[class*='Modal_modal_opened'] div[class*='Modal_modal__contentBox']") # попап заказа в ленте заказов


