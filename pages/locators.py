from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")  # форма авторизации
    REGISTER_FORM = (By.ID, "register_form")  # Форма регистрации
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")  # Ввод email для регистрации
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")  # Ввод пароля для регистрации
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")  # Ввод подтв. пароля для регистрации
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, ".btn[name='registration_submit']")  # Кнопка регистрации


class ProductPageLocators:
    BUTTON_ADD_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")  # Кнопка добавления в корзину
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, "div.product_main h1")  # Имя товара в корзине
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")  # Сообщение о добавлении товара в корзину
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")  # Цена товара
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")  # Цена товара в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")  # Сообщение об успешном добавлении товара в корзину


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # Кнопка авторизации/регистрации пользователя
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")  # Неправильная кнопка авторизации/регистрации поль.
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")  # Кнопка корзины
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")  # Сообщение авторизации пользователя


class BasketLocators:
    PRODUCT_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")  # Сообщение об отсутствии товара
