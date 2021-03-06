"""Test different web elements in Product page"""
import pytest
import allure
from PageObject import ProductPage, CartPage

@allure.description("Different test cases with some functional in Product")
@pytest.mark.parametrize('qty', ['10'], ids=['quantity=10'])
def test_product_quantity(browser_driver, get_url, my_logger, qty):
    """Test for input in quantity field"""
    my_logger.info('Input quantity for Product')
    ProductPage(browser_driver) \
        .open_product_page() \
        .quantity(qty)
    qty_value = browser_driver.find_element(*ProductPage.QUANTITY).get_attribute('value')

    assert str(qty_value) == str(qty)


def test_add_to_card_button(browser_driver, get_url):
    """Test for Add to Card button"""
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()


def test_rating_stage(browser_driver, get_url):
    """Test for rating stage"""
    ProductPage(browser_driver).open_product_page() \
        .rating()


def test_add_product_to_cart(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_view_cart()

    assert browser_driver.title == 'Shopping Cart'


def test_product_checkout(browser_driver, get_url):
    ProductPage(browser_driver) \
        .open_product_page() \
        .add_to_card()
    CartPage(browser_driver) \
        .open_cart() \
        .click_checkout_cart()
