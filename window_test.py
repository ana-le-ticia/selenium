from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

def wait_element(by, path):
    WebDriverWait(browser,60).until(
        EC.element_to_be_clickable((by,path))
    )

def open_window(url):
    browser.get(url)

url_list = [
    'https://brasilescola.uol.com.br/',
    'https://web.whatsapp.com/',
    'https://www.instagram.com/brasilescolaoficial/'
]

for url in url_list:
    open_window(url)
    browser.switch_to.new_window('tab')

current_url = browser.current_url
window_handles = browser.window_handles

def find_expecific_window(palavra: str):
    for window in window_handles:
        browser.switch_to.window(window)
        if palavra in browser.current_url:
            print(f'ENCONTREI!!!!!{browser.current_url}')
            return True
    print(f'Nao foi possivel encontrar a palavra {palavra}')
    return False

find_expecific_window('brasilescola')

print(browser.current_url)
print(browser.window_handles)

browser.quit()


