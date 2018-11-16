#! Python 3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, time

# Open Browser
browser = webdriver.Firefox()
browser.get('http://gmail.com')

# Input email and hit next
browser.find_element_by_id('identifierId').send_keys('luvsicpart10')
browser.find_element_by_id('identifierNext').click()

# Wait up to 10seconds for PW form to be interactable input password and hit next
# wait = WebDriverWait(browser, 10) # Wait up to 10 seconds in case something goes wrong
# pwElem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')))
time.sleep(1)
browser.find_element_by_css_selector('input[class="whsOnd zHQkBf"]').send_keys('Sh1kinouta')
browser.find_element_by_id('passwordNext').click()

browser.find_element_by_css_selector('div[class="T-I J-J5-Ji T-I-KE L3"]').click()


browser.find_element_by_css_selector('textarea[id=":le"]').send_keys('glee@lji.org') # Element will not appear until click event