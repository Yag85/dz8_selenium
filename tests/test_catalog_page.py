"""Test for different web element in Catalog page"""
import pytest
import allure
from PageObject.CatalogPage import CatalogPage

@allure.title('Test for List View button')
def test_list_view_button(browser_driver, get_url):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .list_button_active()

@allure.title('Test for Grid View button')
def test_grid_view_button(browser_driver, get_url):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .grid_button_active()

@allure.title('Test for Sorting')
@pytest.mark.parametrize('sort_option', ['Rating (Lowest)'])
def test_checking_sort_by(browser_driver, get_url, sort_option):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .select_from_sort_by(sort_option)

    check_result = browser_driver.find_element(*CatalogPage.SORT_BY_SELECTED).text

    assert str(check_result) == str(sort_option)

@allure.title('Test on the show value')
@pytest.mark.parametrize('show_option', ['100'])
def test_checking_show_value(browser_driver, get_url, show_option):
    CatalogPage(browser_driver) \
        .open_catalog_page() \
        .select_show_element(show_option)

    check_result = browser_driver.find_element(*CatalogPage.SHOW_VALUE_SELECTED).text

    assert str(check_result) == str(show_option)
