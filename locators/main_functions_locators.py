from selenium.webdriver.common.by import By


class MainFunctionsLocators:
    PERSONAL_ACC = [By.XPATH, "//p[text()='Личный Кабинет']"]  # кнопка Личный Кабинет
    CONSTRUCTOR = [By.XPATH, "//p[text()='Конструктор']"]  # кнопка Конструктор
    ORDERS_LINE = [By.XPATH, "//p[text()='Лента Заказов']"]  # кнопка Лента Заказов
    INGREDIENT = [By.XPATH, "//img[@alt='Краторная булка N-200i']"]  # ингредиент Краторная булка
    INGREDIENT_WINDOW = [By.XPATH, "//h2[text()='Детали ингредиента']"]  # всплывающее окно с деталями ингредиента
    CROSS_ON_INGREDIENT_WINDOW = [By.CSS_SELECTOR, 'section.Modal_modal_opened__3ISw4 '
                                                   'button.Modal_modal__close_modified__3V5XS svg > path']  # крестик на окне ингредиента
    COUNTER = [By.XPATH, "(//ul[contains(@class,'BurgerIngredients_ingredients__list')]/a)[2]//div[contains(@class,'counter_counter__ZNLkj')]"]  # каунтер ингредиента
    MOVE_INGREDIENT = [By.XPATH, "//span[contains(text(),'(верх)')]"]  # место, в которое нужно перетащить ингредиент
    MAKE_ORDER = [By.XPATH, "//button[text()='Оформить заказ']"]  # кнопка оформления заказа
    ORDER_CONFIRMATION_SCREEN = [By.CSS_SELECTOR, 'h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text_type_digits-large.mb-8']  # экран подтверждения заказа
    OVERLAY = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"] #элемент загрузки
    ORDER_POPUP_CROSS = [By.CSS_SELECTOR, 'path[fill-rule="evenodd"][clip-rule="evenodd"][d^="M3.29289 3.29289"]'] # крест на окне подтверждения заказа
