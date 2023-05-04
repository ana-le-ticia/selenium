from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service 
from time import sleep

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

url = 'https://www.lottemart.com'

browser.get(url)

browser.find_element('xpath','//*[@class="popupClose"]').click() #isso sim

#isso nao funciona
alert = browser.switch_to.alert
sleep(2)
alert.accept()

# browser.refresh()
