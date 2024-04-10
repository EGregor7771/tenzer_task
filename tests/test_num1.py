from selenium.webdriver.common.by import By
from pages.page_sbis_ru import PageSBISRu
from pages.page_sbis_ru_contacts import PageSBISRuSverdObl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.page_tensor_ru import PageTensorRu
from pages.page_tensor_ru_about import PageTensorRuAbout

url_contacts_common = 'https://sbis.ru/contacts'
url_contacts_sverd_obl = 'https://sbis.ru/contacts/66-sverdlovskaya-oblast?tab=clients'
url_tensor = 'https://tensor.ru/'
url_tensor_about = 'https://tensor.ru/about'


def test_click_button_contacts(browser):
    page = PageSBISRu(browser)
    page.open()
    page.check_banner_contacts()
    page.click_banner_contacts()
    wait = WebDriverWait(browser, 5)
    wait.until(EC.url_changes(url_contacts_common))
    assert browser.current_url == url_contacts_sverd_obl


def test_banner_tensor_click(browser):
    page = PageSBISRuSverdObl(browser)
    page.open()
    page.check_banner_tensor()
    page.click_banner_tensor()
    page.open2window()
    assert browser.current_url == url_tensor


def test_banner_power_to_people(browser):
    page = PageTensorRu(browser)
    page.open()
    page.find_block_power()
    assert browser.current_url == url_tensor_about


def test_check_height_width(browser):
    page = PageTensorRuAbout(browser)
    page.open()
    block = page.find_block_power()
    images = block.find_elements(By.TAG_NAME, 'img')
    width, height = images[0].size['width'], images[0].size['height']
    for image in images:
        assert width == image.size['width'] and height == image.size['height']

