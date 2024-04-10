from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains

banner_selector = (By.XPATH, '//div[@class="tensor_ru-Index__block4-bg"]/descendant::a[@class="tensor_ru-link tensor_ru-Index__link"]')


class PageTensorRu(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url_page = 'https://tensor.ru/'

    def open(self):
        self.browser.get(self.url_page)

    def find_block_power(self):
        block = self.find(banner_selector)
        ActionChains(self.browser).scroll_to_element(block).perform()
        ActionChains(self.browser).scroll_by_amount(0, 50).perform()
        ActionChains(self.browser).move_to_element(block).perform()
        block.click()
