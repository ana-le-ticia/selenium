from functools import partial
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)


url = 'https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#'

browser.get(url)
browser.maximize_window()

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


def wait_element(by,element_by,webdriver):
    element = webdriver.find_element(by,element_by)
    return bool(element)

wait = WebDriverWait(browser,60)

for i in range(4):

    text_xpath = '/html/body/div/header/p[3]'

    wait_name = partial(wait_element, 'xpath', xpath_name_forms[i])
    wait.until(
    partial(wait_name), 'element not found'
    )

    wait_pas_word = partial(wait_element, 'xpath', xpath_pass_word_forms[i])
    wait.until(
    partial(wait_pas_word), 'element not found'
    )

    wait_text = partial(wait_element, 'xpath', text_xpath)
    wait.until(
    partial(wait_element, 'xpath', text_xpath), 'element not found'
    )

    texto_antes = browser.find_element('xpath',text_xpath).text

    fill_form(xpath_name_forms[i],xpath_pass_word_forms[i],list_names[i],list_pass_word[i],list_button_xpath[i])

    texto_depois = browser.find_element('xpath',text_xpath).text
    
    wait_text = partial(wait_element, 'xpath', text_xpath)
    wait.until(
    partial(wait_element, 'xpath', text_xpath), 'element not found'
    )

    assert texto_antes == texto_depois

    print(texto_antes)
    print(texto_depois)


# print(browser.find_element('xpath',text_xpath).text)

# fill_form(xpath_name_forms[0],xpath_pass_word_forms[0],list_names[0],list_pass_word[0],list_button_xpath[0])
# assert texto == browser.find_element('xpath',text_xpath).text

# fill_form(xpath_name_forms[1],xpath_pass_word_forms[1],list_names[1],list_pass_word[1],list_button_xpath[1])
# assert texto == browser.find_element('xpath',text_xpath).text

# fill_form(xpath_name_forms[2],xpath_pass_word_forms[2],list_names[2],list_pass_word[2],list_button_xpath[2])
# assert texto == browser.find_element('xpath',text_xpath).text

# fill_form(xpath_name_forms[3],xpath_pass_word_forms[3],list_names[3],list_pass_word[3],list_button_xpath[3])
# assert texto == browser.find_element('xpath',text_xpath).text


browser.quit()
