from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketLocators.PRODUCT_IS_EMPTY), "Product should not be in backet"

    def message_basket_is_empty(self):
        assert self.browser.find_element(*BasketLocators.PRODUCT_IS_EMPTY).text == \
               'Ваша корзина пуста Продолжить покупки', "Message about empty basket is not"
