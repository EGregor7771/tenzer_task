from selenium.webdriver.common.by import By
from pages.base_page import BasePage

banner_selector = (By.XPATH, '//li[@class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]')


class PageSBISRu(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url_page = 'https://sbis.ru/'

    def open(self):
        self.browser.get(self.url_page)

    def check_banner_contacts(self):
        return self.find(banner_selector)

    def click_banner_contacts(self):
        return self.find(banner_selector).click()
