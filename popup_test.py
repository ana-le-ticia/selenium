from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

s = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=s)

url = 'https://brasilescola.uol.com.br/'

browser.get(url)

main_window = browser.current_window_handle


buton_element = WebDriverWait(browser,60).until(
        EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/header/div[1]/div[1]/div/a[4]'))
    )

link_element = browser.find_element(By.XPATH,'/html/body/div[2]/header/div[1]/div[1]/div/a[4]')
link_element.click()


while len(browser.window_handles) == 1:
    continue

for window_handle in browser.window_handles:
    if window_handle != main_window:
        browser.switch_to.window(window_handle)
        break


print(browser.title)
# sleep(2)
# input_xpath = 'html._9dls.js-focus-visible._aa4c body._a3wf._-kb div#mount_0_0_7I div div div.x9f619.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6.x1ja2u2z div.x78zum5.xdt5ytf.x1n2onr6 div.x78zum5.xdt5ytf.x1n2onr6.xat3117.xxzkxad div.x78zum5.xdt5ytf.x10cihs4.x1t2pt76.x1n2onr6.x1ja2u2z div section.x78zum5.xdt5ytf.x1iyjqo2.xg6iff7.x6ikm8r.x10wlt62 nav._acbh._acbi._acbk div._acc1._acc3 div._acum div._acun div._aawf._aawg._aexm input._aauy'
# input_insta = browser.find_element(By.XPATH,input_xpath)

# input_insta.send_keys('@jungkook')
