from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

s = Service(GeckoDriverManager().install())

driver = webdriver.Firefox(service=s)
url = 'https://selenium.dunossauro.live/aula_09_a.html'
wdw = WebDriverWait

def wait_name(webdriver):
    nome = webdriver.find_elements('id' 'request')
    return bool(nome)
