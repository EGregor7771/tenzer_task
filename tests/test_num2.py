from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.page_sbis_ru import PageSBISRu
from pages.page_sbis_ru_contacts import PageSBISRuSverdObl
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url_contacts_common = 'https://sbis.ru/contacts'
url_contacts_sverd_obl = 'https://sbis.ru/contacts/66-sverdlovskaya-oblast?tab=clients'
url_contacts_kam_krai = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'

local_position = 'Свердловская обл.'
new_position = 'Камчатский край'

partner_sverd_obl_selector = (By.XPATH, '//div[@title="СБИС - Екатеринбург"]')
partner_kam_krai_selector = (By.XPATH, '//div[@title="СБИС - Камчатка"]')
new_position_selector = (By.XPATH, '//span[@title="Камчатский край"]')
regions_selector = (By.NAME, 'dialog')
block_regions = (By.CLASS_NAME, 'sbis_ru-Region-Panel__item')
desired_region = '41 Камчатский край'


def test_contacts_local_position(browser):
    page = PageSBISRu(browser)
    page.open()
    page.check_banner_contacts()
    page.click_banner_contacts()
    wait = WebDriverWait(browser, 5)
    wait.until(EC.url_changes(url_contacts_common))
    assert browser.current_url == url_contacts_sverd_obl


def test_local_position(browser):
    page = PageSBISRuSverdObl(browser)
    page.open()
    partner = page.find(partner_sverd_obl_selector).text
    position = page.get_local_position()
    assert local_position == position.text
    position.click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.element_to_be_clickable(block_regions))

    list_regions = page.find(regions_selector).find_elements(By.CLASS_NAME, 'sbis_ru-Region-Panel__item')
    for region in list_regions:
        if region.find_element(By.XPATH, './/span').text == desired_region:
            ActionChains(page.browser).scroll_to_element(region).perform()
            region.click()
            break

    assert partner != page.find(partner_kam_krai_selector).text
    assert new_position == page.get_local_position().text
    assert browser.current_url == url_contacts_kam_krai
