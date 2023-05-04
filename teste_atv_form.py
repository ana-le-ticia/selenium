from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

wdw = WebDriverWait

def wait_name(webdriver):
    nome = webdriver.find_elements('tag_name' 'input')
    return bool(nome)

wdw.until(wait_name,10)

url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#'

browser.get(url)

xpath_name_forms = [
    '//*[@class="form-l0c0"]//input[@name="nome"]',
    '//*[@class="form-l0c1"]//input[@name="nome"]',
    '//*[@class="form-l1c0"]//input[@name="nome"]',
    '//*[@class="form-l1c1"]//input[@name="nome"]'
]
xpath_pass_word_forms = [
    '//*[@class="form-l0c0"]//input[@name="senha"]',
    '//*[@class="form-l0c1"]//input[@name="senha"]',
    '//*[@class="form-l1c0"]//input[@name="senha"]',
    '//*[@class="form-l1c1"]//input[@name="senha"]'
]

list_names = [
    'ana',
    'leticia',
    'maciel',
    'costa'
]
list_pass_word = [
    '123_ana',
    '123_leticia',
    '123_maciel',
    '123_costa',
]
list_button_xpath = [
    '//*[@class="form-l0c0"]//input[@type="submit"]',
    '//*[@class="form-l0c1"]//input[@type="submit"]',
    '//*[@class="form-l1c0"]//input[@type="submit"]',
    '//*[@class="form-l1c1"]//input[@type="submit"]'
]

def fill_form(name_xpath, pass_word_xpath, name, pass_word, button_xpath):
    form_name = browser.find_element('xpath',name_xpath)
    form_name.send_keys(name)
    form_pass_word = browser.find_element('xpath',pass_word_xpath)
    form_pass_word.send_keys(pass_word)
    form_button = browser.find_element('xpath',button_xpath)
    form_button.click()

sleep(2)

fill_form(xpath_name_forms[0],xpath_pass_word_forms[0],list_names[0],list_pass_word[0],list_button_xpath[0])
fill_form(xpath_name_forms[1],xpath_pass_word_forms[1],list_names[1],list_pass_word[1],list_button_xpath[1])
fill_form(xpath_name_forms[2],xpath_pass_word_forms[2],list_names[2],list_pass_word[2],list_button_xpath[2])
fill_form(xpath_name_forms[3],xpath_pass_word_forms[3],list_names[3],list_pass_word[3],list_button_xpath[3])

sleep(2)

browser.quit()














# # PRENCHER TODOS O NOME DE TODOS OS FORMS(NAO ENVIA)
# for i,xpath_name in enumerate (xpath_name_forms):
#     browser.find_element('xpath',xpath_name).send_keys(list_names[i])

#PRENCHER TODAS AS SENHAS DE TODOS OS FORMS(NAO ENVIA)
# for i,xpath_password in enumerate (xpath_pass_word_forms):
#     browser.find_element('xpath',xpath_password).send_keys(list_pass_word[i])

# PREENCHER 1 FORM 4 VEZES E ENVIAR UM DE CADA VEZ
# for i,name in enumerate(list_names):
#     browser.find_element('xpath','//*[@class="form-l0c0"]//input[@name="nome"]').send_keys(name)
#     browser.find_element('xpath','//*[@class="form-l0c0"]//input[@name="senha"]').send_keys(list_pass_word[i])
#     browser.find_element('xpath','//*[@class="form-l0c0"]//input[@type="submit"]').click()

# for i,xpath_name in enumerate(xpath_name_forms):
#     browser.find_element('xpath',xpath_name).send_keys('ana')
#     browser.find_element('xpath',i).send_keys('123_ana')
#     sleep(2)
#     browser.find_element('xpath','//*[@class="form-l0c0"]//input[@type="submit"]').click()

# name_form_1 = browser.find_element('xpath','//form[contains(@class,"form-l0c0")]//input[contains(@name,"nome")]')
# name_form_1.send_keys('Ana')
# # sleep(2)
# pass_word_form_1 = browser.find_element('xpath','//form[contains(@class,"form-l0c0")]//input[contains(@name,"senha")]')
# pass_word_form_1.send_keys('123_ana')
# # sleep(2)
# browser.find_element('xpath','//*[@class="form-l0c0"]//input[@type="submit"]').click()
# # sleep(2)

# resultado = browser.find_element('xpath','//div/h2').text
# assert 'Resultado' == resultado

# name_form_2 = browser.find_element('xpath','//form[contains(@class,"form-l0c1")]//input[contains(@name,"nome")]')
# name_form_2.send_keys('Letícia')
# # sleep(2)
# pass_word_form_2 = browser.find_element('xpath','//form[contains(@class,"form-l0c1")]//input[contains(@name,"senha")]')
# pass_word_form_2.send_keys('123_leticia')
# # sleep(2)
# browser.find_element('xpath','//*[@class="form-l0c1"]//input[@type="submit"]').click()
# # sleep(2)
# resultado = browser.find_element('xpath','//div/h2').text
# assert 'Resultado' == resultado

# name_form_3 = browser.find_element('xpath','//form[contains(@class,"form-l1c0")]//input[contains(@name,"nome")]')
# name_form_3.send_keys('Maciel')
# # sleep(2)
# pass_word_form_3 = browser.find_element('xpath','//form[contains(@class,"form-l1c0")]//input[contains(@name,"senha")]')
# pass_word_form_3.send_keys('123_maciel')
# # sleep(2)
# browser.find_element('xpath','//*[@class="form-l1c0"]//input[@type="submit"]').click()
# # sleep(2)
# resultado = browser.find_element('xpath','//div/h2').text
# assert 'Resultado' == resultado

# name_form_4 = browser.find_element('xpath','//form[contains(@class,"form-l1c1")]//input[contains(@name,"nome")]')
# name_form_4.send_keys('Costa')
# # sleep(2)
# pass_word_form_4 = browser.find_element('xpath','//form[contains(@class,"form-l1c1")]//input[contains(@name,"senha")]')
# pass_word_form_4.send_keys('123_costa')
# # sleep(2)
# browser.find_element('xpath','//*[@class="form-l1c1"]//input[@type="submit"]').click()
# # sleep(2)

