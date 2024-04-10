from selenium.webdriver.common.by import By
from pages.base_page import BasePage

banner_selector = (By.XPATH, '//a[@title="tensor.ru"]')
position_selector = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')


class PageSBISRuSverdObl(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url_page = 'https://sbis.ru/contacts/66-sverdlovskaya-oblast?tab=clients'

    def open(self):
        self.browser.get(self.url_page)

    def check_banner_tensor(self):
        return self.find(banner_selector)

    def click_banner_tensor(self):
        return self.find(banner_selector).click()

    def get_local_position(self):
        return self.find(position_selector)