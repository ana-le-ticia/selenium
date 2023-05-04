from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=s)

URL = 'https://selenium.dunossauro.live/aula_09_a.html'

# wdw = WebDriverWait

def find_box(browser):
    browser.get(URL)
    element = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located(('id','request'))
    )
    browser.find_element('id','request').click()
    return bool(element)

def check_text(browser):
    browser.get(URL)
    WebDriverWait(browser, 60).until(
        EC.presence_of_element_located(('id','finished'))
    )
    text_element = browser.find_element('id','finished').text
    assert text_element == 'Carregamento concluído'

    return bool(text_element)


find_box(browser)


