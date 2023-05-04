from selenium import webdriver 
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install()) #busca e instala a versao atual correspondente ao driver

browser = webdriver.Firefox(service=service) #criou o navegador

browser.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")

browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Ana Leticia")

browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('anaharu03@gmail.com')

browser.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/div[2]/form/button/span/b').click()

#firefox - geckodriver
#geckodriver_manager busca a versao mais atual do nosso navegador, instala e usa ela
#automatiza o processo de buscar e instalar manualmente o navegador mais recente
#service executa o geckodriver_manager

#.click() clicar no elemento
#.send_keys() escreve no elemento
#.get("linkCompletoDaPag") permite vc a ir para uma pag especifica
#.find_element() permite achar um elemento dentro da pagina html