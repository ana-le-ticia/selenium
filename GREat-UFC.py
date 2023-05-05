from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from functools import partial
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

s = Service(GeckoDriverManager().install())

browser = webdriver.Firefox(service=s)

url = 'https://github.com/LuizHenriqueVitorino/python-selenium-notas-de-aula/blob/main/atividades.md'

browser.get(url)
browser.maximize_window()

def wait_element(by, path):
    WebDriverWait(browser,10).until(
        EC.presence_of_element_located((by,path))
    )

test_link_pag_path = '.markdown-body > ol:nth-child(5) > li:nth-child(1) > a:nth-child(1)'
wait_element(By.CSS_SELECTOR,test_link_pag_path)
test_link_pag = browser.find_element(By.CSS_SELECTOR,test_link_pag_path)
test_link_pag.click()

test_link_pag_url = 'https://testlink.org/'
assert test_link_pag_url == browser.current_url, 'Não está na pagina do github'

great_git_repo_path = '//a[contains(text(),"Access Git Repository (GitHub)")]'
wait_element(By.XPATH,great_git_repo_path)
great_git_repo = browser.find_element(By.XPATH,great_git_repo_path)
great_git_repo.click()

great_git_repo_url = 'https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/'
assert great_git_repo_url == browser.current_url, 'Não está na pagina do github do great'

search_bar_path = "//*[@class='form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field js-site-search-field is-clearable']"
wait_element(By.XPATH,search_bar_path)
search_bar = browser.find_element(By.XPATH,search_bar_path)
search_bar.send_keys('LuizHenriqueVitorino')
search_bar.send_keys(Keys.ENTER)

print('pasou')

# browser.quit()

