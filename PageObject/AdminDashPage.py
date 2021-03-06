"""Selectors for different elements in the Opencart admin page """
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from PageObject.BasePage import BasePage


class AdminDashboard(BasePage):
    class Navigation:
        CATALOG = (By.XPATH, '//li[@id="menu-catalog"]/a[contains(text(), "Catalog")]')
        CATALOG_PRODUCTS = (By.XPATH, '//ul[@id="collapse1"]/li/a[contains(text(), "Products")]')
        CATALOG_OPTIONS = (By.XPATH, '//ul[@id="collapse1"]/li/a[contains(text(), "Options")]')

    class GeneralActions:
        ADD_NEW = (By.CSS_SELECTOR, 'a[data-original-title="Add New"]')
        EDIT = (By.CSS_SELECTOR, "a[data-original-title='Edit']")
        COPY = (By.CSS_SELECTOR, "button[data-original-title='Copy']")
        REMOVE = (By.CSS_SELECTOR, "button[data-original-title='Delete']")
        SAVE = (By.CSS_SELECTOR, "button[data-original-title='Save']")
        CANCEL = (By.CSS_SELECTOR, "a[data-original-title='Cancel']")
        CHECK_FOR_REMOVE = (By.XPATH, "//table//tr[2]/td/input[@type='checkbox']")
        SUCCESS_TEXT = (By.XPATH, "//div[contains(text(), 'Success')]")

    class ProductForm:
        PRODUCT_NAME = (By.CSS_SELECTOR, '#input-name1')
        META_TAG_TITLE = (By.CSS_SELECTOR, '#input-meta-title1')
        PRODUCT_TAG = (By.CSS_SELECTOR, '#input-tag1')
        MODEL = (By.CSS_SELECTOR, '#input-model')
        IMAGE = (By.XPATH, "//div[@id='tab-image']//a/img")
        EDIT_IMAGE = (By.XPATH, "//button[@id='button-image']")
        UPLOAD_IMAGE = (By.XPATH, "//button[@data-original-title='Upload']")
        CHOOSE_FILE = (By.CSS_SELECTOR, "input[type='file']")
        CLOSE_UPLOAD_WINDOW = (By.XPATH, "//button[contains(text(), '×')]")

        class ProductTabs:
            DATA_TAB = (By.XPATH, '//*[@id="form-product"]//li/a[contains(text(), "Data")]')
            IMAGE_TAB = (By.XPATH, '//*[@id="form-product"]//li/a[contains(text(), "Image")]')

    class OptionsForm:
        OPTION_NAME = (By.CSS_SELECTOR, '.input-group input')
        TYPE = (By.XPATH, "//select[@id='input-type']")
        SORT_ORDER = (By.CSS_SELECTOR, '#input-sort-order')
        ADD_OPTION_VALUE = (By.CSS_SELECTOR, 'button[data-original-title="Add Option Value"]')
        REMOVE_OPTION_VALUE = (By.CSS_SELECTOR, 'button[title="Remove"]')
        OPTION_VALUE_NAME = (By.CSS_SELECTOR, '#option-value .input-group input')

    def open_product_from_catalog(self):
        self._click_to_element(self.Navigation.CATALOG)
        self._click_to_element(self.Navigation.CATALOG_PRODUCTS)
        return self

    def open_options_from_catalog(self):
        self._click_to_element(self.Navigation.CATALOG)
        self._click_to_element(self.Navigation.CATALOG_OPTIONS)
        return self

    def add_new_element(self):
        self._click_to_element(self.GeneralActions.ADD_NEW)
        return self

    def edit_element(self):
        self._click_to_element(self.GeneralActions.EDIT)
        return self

    def save_element(self):
        self._click_to_element(self.GeneralActions.SAVE)
        return self

    def copy_element(self):
        self._click_to_element(self.GeneralActions.CHECK_FOR_REMOVE)
        self._click_to_element(self.GeneralActions.COPY)
        return self

    def remove_element(self):
        self._click_to_element(self.GeneralActions.CHECK_FOR_REMOVE)
        self._click_to_element(self.GeneralActions.REMOVE)
        return self

    def input_product_form_general_tab(self, prod_name, meta_tag):
        self._send_keys(prod_name, self.ProductForm.PRODUCT_NAME)
        self._send_keys(meta_tag, self.ProductForm.META_TAG_TITLE)
        return self

    def input_product_form_data_tab(self, model):
        self._click_to_element(self.ProductForm.ProductTabs.DATA_TAB)
        self._send_keys(model, self.ProductForm.MODEL)
        return self

    def upload_new_image(self):
        self._click_to_element(self.ProductForm.ProductTabs.IMAGE_TAB)
        self._click_to_element(self.ProductForm.IMAGE)
        self._click_to_element(self.ProductForm.EDIT_IMAGE)
        self._wait_for_visible(self.ProductForm.UPLOAD_IMAGE)
        self._click_to_element(self.ProductForm.UPLOAD_IMAGE)
        return self

    def select_image_from_explorer(self):
        # Change working directory for open config file
        filename = os.path.abspath('selenium.png')
        print(filename)
        choose_file = self.driver.find_element(*self.ProductForm.CHOOSE_FILE)
        choose_file.send_keys(filename)
        time.sleep(5)
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    def close_upload_window(self):
        self._click_to_element(self.ProductForm.CLOSE_UPLOAD_WINDOW)
        return self

    def input_options_form(self, option_name, type=None, sort_order=None):
        self._send_keys(option_name, self.OptionsForm.OPTION_NAME)
        if type != None and sort_order != None:
            self._send_keys(type, self.OptionsForm.TYPE)
            self._send_keys(sort_order, self.OptionsForm.SORT_ORDER)
        return self

    def add_option_value(self, value_name):
        self._click_to_element(self.OptionsForm.ADD_OPTION_VALUE)
        self._wait_for_visible(self.OptionsForm.OPTION_VALUE_NAME)
        self._send_keys(value_name, self.OptionsForm.OPTION_VALUE_NAME)
        return self

