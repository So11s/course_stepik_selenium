import math

from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def go_to_product_page(self):
        button_add = self.browser.find_element(*ProductPageLocator.BUTTON_ADD_LINK)
        button_add.click()

    def should_be_product_on_page(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_LINK).text
        assert self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_LINK), "Product name is not presented"
        assert self.browser.find_element(*ProductPageLocator.BUTTON_ADD_LINK), "Add button is not presented"
        return product_name

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocator.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocator.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(*ProductPageLocator.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"
        assert self.should_be_product_on_page() == \
               self.browser.find_element(*ProductPageLocator.PRODUCT_NAME_IN_BASKET).text, (
            "Incorrect name product in basket")

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
