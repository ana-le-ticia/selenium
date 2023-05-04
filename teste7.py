from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert
from time import sleep

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)
url = 'https://selenium.dunossauro.live/aula_11_a.html'

browser.get(url)

# alerta = browser.find_element('id','alert')
# sleep(3)
# alerta.click()
# sleep(2)
# alert = Alert(browser)
# sleep(2)
# alert.accept()
# sleep(3)

element = browser.find_element('id','alert')
sleep(2)
alert = Alert(browser)
sleep(2)
alert.send_keys('kkk')
sleep(3)

browser.quit()
