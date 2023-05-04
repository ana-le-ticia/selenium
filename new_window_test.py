from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# from selenium.webdriver.common.alert import Alert

s = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=s)

url = 'https://brasilescola.uol.com.br/'

browser.get(url)
browser.maximize_window()

current_window = browser.current_window_handle

insta_element = WebDriverWait(browser,60).until(
        EC.element_to_be_clickable(('xpath','/html/body/div[2]/header/div[1]/div[1]/div/a[4]'))
    )

insta_link = browser.find_element('xpath','/html/body/div[2]/header/div[1]/div[1]/div/a[4]')
insta_link.click()
sleep(2)

handles = []
handles = browser.window_handles

new_handle = handles[1]
browser.switch_to.window(new_handle)

#second window
search_bar_element = WebDriverWait(browser,60).until(
        EC.presence_of_element_located(('xpath','/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/input'))
    )
sleep(8)
search_bar_insta = browser.find_element('xpath','/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/input')
search_bar_insta.send_keys('ola')