from selenium.webdriver.common.by import By


class OrdersLineLocators:
    ORDER = [By.XPATH, "//*[@id='root']/div/main/div/div/ul/li[1]/a/div[1]/p[1]"] # первый заказ  в ленте"
    ORDER_HISTORY_SCREEN = [By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[last()]/a/div[1]/p[1]"] #заказ со страницы Истории Заказов
    ALL_TIME_COUNTER = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] # счетчик за все время
    TODAY_COUNTER = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] # счетчик за сегодня
    IN_PROGRESS = (By.XPATH, "//*[@id='root']/div/main/div/div/div/div[1]/ul[2]/li") # первое значение в списке В работе
    ORDER_POPUP_SCREEN = [By.XPATH, "//*[@id='root']/div/section[2]/div[1]/div"] # попап заказа в ленте заказов


