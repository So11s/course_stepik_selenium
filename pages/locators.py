from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    BUTTON_ADD_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")


class BasketLocators:
    PRODUCT_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")