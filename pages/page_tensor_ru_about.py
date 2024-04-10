from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

base_selector = (By.CLASS_NAME, 'tensor_ru-About__block3')


class PageTensorRuAbout(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url_page = 'https://tensor.ru/about'

    def open(self):
        self.browser.get(self.url_page)

    def find_block_power(self):
        block = self.find(base_selector)
        ActionChains(self.browser).scroll_to_element(block).perform()
        ActionChains(self.browser).scroll_by_amount(0, 50).perform()
        return block
