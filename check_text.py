from functools import partial
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


s = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=s)

url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=gry&senha=ygtr&l0c0=Enviar%21#'
browser.get(url)

def explicitWait(by,way):
    try: 
        element = WebDriverWait(browser, 60).until( 
            ec.visibility_of((by,way)) 
        ) 
    except: 
        browser.quit() 
    return bool(element)


num_ = '//*[@id="num"]'

print(explicitWait('xpath',num_))
num_de_vdd0 = browser.find_element('xpath',num_)

# print(explicitWait('xpath','/html/body/div/div/textarea'))
# text_bef_act = browser.find_element('xpath','/html/body/div/div/textarea').text

# find_name = browser.find_element('xpath','//*[@class="form-l0c0"]//input[@name="nome"]').send_keys('oi')
# find_passWord = browser.find_element('xpath','//*[@class="form-l0c0"]//input[@name="senha"]').send_keys('123')
# find_button = browser.find_element('xpath','//*[@class="form-l0c0"]//input[@type="submit"]').click()

# print(explicitWait('xpath',num_))
# num_de_vdd = browser.find_element('xpath',num_)

# print(explicitWait('xpath','/html/body/div/div/textarea'))
# text_aft_act = browser.find_element('xpath','/html/body/div/div/textarea').text

# print(text_bef_act)
# print(text_aft_act)
print(num_de_vdd0.text)
# s



