from selenium.webdriver.common.by import By


class PasswordLocators:
    RESET_PASS_LINK = [By.XPATH, "//a[text()='Восстановить пароль']"]  # ссылка Восстановить пароль
    RECOVER_PASS_BUTTON = [By.XPATH, "//button[text()='Восстановить']"] # кнопка Восстановить
    EMAIL_FIELD_PASS = [By.CSS_SELECTOR, 'input.input__textfield[name="name"]'] # поле email на странице восстановления пароля
    EYE_ICON = [By.CSS_SELECTOR, 'path[d^="M12 4C14.0683 4"]'] # иконка глаза
    PASSWORD_FIELD_EYE = [By.CSS_SELECTOR, 'div.input_type_text.input_status_active'] # поле пароль на странице восстановления пароля


