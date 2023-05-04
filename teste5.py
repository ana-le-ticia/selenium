from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()

browser.get('https://selenium.dunossauro.live/aula_07_d')

input_text = browser.find_element(By.TAG_NAME,"input")
span = browser.find_element(By.TAG_NAME,"span")
p = browser.find_element(By.TAG_NAME,"p")

input_text.click()
assert 'esta com foco' == span.text, 'esta com foco'
span.click()
assert 'esta sem foco' == span.text, 'esta sem foco'

browser.quit()