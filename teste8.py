from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service 
from time import sleep


service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

url = 'https://omayo.blogspot.com/'
browser.get(url)

browser.find_element('id','alert1').click()

alert = browser.switch_to.alert
sleep(2)
alert.accept()

text_box = browser.find_element('xpath','/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[3]/div[1]/textarea')
text_box.clear()
sleep(1)

n = 0
while n!=3:
    text_box.send_keys(f'teste {n+1}\n')
    n += 1

sleep(3)
browser.quit()