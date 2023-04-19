from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=0):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """переходит на страницу"""

        self.browser.get(self.url)

    def go_to_login_page(self):
        """ кликает на кнопку авторизации/регистрации пользователя """

        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        """кликает на кнопку корзины"""

        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_login_link(self):
        """проверка на наличие кнопки авторизации/регистрации пользователя"""

        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        """проверка успешной авторизации пользователя"""

        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def is_element_present(self, how, what):
        """проверяет наличие элемента и возвращает bool"""

        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """провряет, что элемент не появляется на странице"""

        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """проверяет, что элемент должен исчезнуть"""

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
