from selenium.webdriver.common.by import By


class OrdersLineLocators:
    ORDER = [By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59 > li:first-child .OrderHistory_dataBox__1mkxK"] # первый заказ  в ленте"
    ORDER_SCREEN = [By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X"]  #всплывающее окно заказа
    ORDER_HISTORY_SCREEN = [By.XPATH, "(//p[contains(@class,'text_type_digits-default')])[1]"] #заказ со страницы Истори Заказов
    ORDER_LINE_SCREEN = [By.XPATH, f"//p[text()='{order_number}']"] # тот же заказ со страницы Ленты Заказов
    ALL_TIME_COUNTER = [By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"] # счетчик за все время
    TODAY_COUNTER = [By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"] # счетчик за сегодня
    IN_PROGRESS_COUNTER = [By.XPATH, f"//li[contains(@class,'text_type_digits-default') and text()='{order_number}']"] #счетчик в работе