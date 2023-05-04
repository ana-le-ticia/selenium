from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

def test_element_demo():
    options = webdriver.FirefoxOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.facbook.com/")

    element_text = driver.find_element(By.TAG_NAME, "h2")
    print(element_text.text)
