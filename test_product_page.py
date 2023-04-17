import pytest

from .pages.product_page import ProductPage

num_promo = [num if num != 7 else pytest.param(num, marks=pytest.mark.xfail) for num in range(10)]


@pytest.mark.parametrize('link', num_promo)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_on_page()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.should_be_message_basket_total()