from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service 


service = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=service)

browser.get('https://selenium.dunossauro.live/exercicio_07.html')
sleep(3)

text = 'Faça seu cadastro'
element_XPATH = '/html/body/div/main/fieldset/legend'
element = browser.find_element('xpath',element_XPATH)
element_text = element.text

assert text == element_text, f'O elemento {element.text} não está presente' 
# print('A frase `Faça seu cadastro` existe')

name_bef_eve = browser.find_element('id','lnome')
name_bef_eve_text =  name_bef_eve.text

browser.find_element('id','nome').send_keys('Ana Letícia')
sleep(1)

name_aft_eve = browser.find_element('id','lnome')
name_aft_eve_text = name_aft_eve.text
assert name_bef_eve_text != name_aft_eve_text, 'Error'

email_bef_eve = browser.find_element('id','lemail')
email_bef_eve_text = email_bef_eve.text

browser.find_element('id','email').send_keys("anaharu03@gmail.com")
sleep(1)

email_aft_eve = browser.find_element('id','lemail')
email_aft_eve_text = email_aft_eve.text
assert email_bef_eve_text != email_aft_eve_text, 'Error'


pass_word_bef_eve = browser.find_element('id','lsenha')
pass_word_bef_eve_text = pass_word_bef_eve.text

browser.find_element('id','senha').send_keys(230804)
sleep(1)

pass_word_aft_eve = browser.find_element('id','lsenha')
pass_word_aft_eve_text = pass_word_aft_eve.text
assert pass_word_bef_eve_text != pass_word_aft_eve_text, 'Error'

browser.find_element('id','btn').click()
sleep(5)
browser.quit()


