from selenium.webdriver.common.by import By


class PrivateAccLocators:
    PERSONAL_ACC = [By.XPATH, "//p[text()='Личный Кабинет']"]  # кнопка Личный Кабинет
    ACC_EMAIL = [By.XPATH, "//input[@type='text']"]  # поле ввода Email
    ACC_PASSWORD = [By.XPATH, "//input[@type='password']"]  # поле ввода Пароль
    ENTER = [By.XPATH, "//button[text()='Войти']"]  # кнопка Войти в форме Войти в аккаунт
    HISTORY_LINK = [By.LINK_TEXT, "История заказов"]  # ссылка на Историю заказов
    EXIT_LINK = [By.XPATH, "//button[text()='Выход']"]  # ссылка Выход
