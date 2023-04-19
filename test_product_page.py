import pytest

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

num_promo = [num if num != 7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10)]


class TestUserAddToBasketFromProductPage:
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_product_page()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_product_page()
        page.should_not_be_success_message_all_time()


@pytest.mark.parametrize('link', num_promo)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}"
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.should_be_product_on_page()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.should_be_message_basket_total()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, timeout=10)
    page.open()
    page.go_to_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link, timeout=10)
    page.open()
    page.go_to_basket_page()
    page.basket_should_be_empty()
    page.message_basket_is_empty()
