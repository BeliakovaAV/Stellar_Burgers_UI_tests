from selenium.webdriver.common.by import By


class OrdersLineLocators:
    ORDER = [By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59 > li:first-child .OrderHistory_dataBox__1mkxK"] # первый заказ  в ленте"
    ORDER_HISTORY_SCREEN = [By.XPATH, "(//p[contains(@class,'text_type_digits-default')])[last()]"] #заказ со страницы Истори Заказов
    ALL_TIME_COUNTER = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] # счетчик за все время
    TODAY_COUNTER = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] # счетчик за сегодня
    IN_PROGRESS = (By.XPATH, "//*[@id='root']/div/main/div/div/div/div[1]/ul[2]/li")
