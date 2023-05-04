from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(GeckoDriverManager().install())
browser = webdriver.Firefox(service=s)

URL = 'https://selenium.dunossauro.live/aula_09_a.html'

# try:
#     buton_element = WebDriverWait(browser,60).until(
#         EC.presence_of_element_located(('id','request'))
#     )
#     browser.find_element('id','request').click()
# except:
#     browser.quit
#     print("Element could not be located") 


wdw = WebDriverWait
def find_element(webdriver):
    name = browser.find_element('id' 'request')
    return bool(name)


# def wait_name(webdriver):
#     nome = webdriver.find_elements('tag_name' 'input')
#     return bool(nome)


# browser.get(URL)
# WebDriverWait(browser, 60).until(
#     find_element
# )


# try:
#     element = WebDriverWait(browser,60).until(
#         EC.presence_of_element_located(('id','finished'))
#     )
#     text_element = browser.find_element('id','finished').text
#     assert text_element == 'Carregamento concluído'
#     browser.quit()
#     print('passou')
# except:
#     browser.quit
#     print("Element could not be located") 