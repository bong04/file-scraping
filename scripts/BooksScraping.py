from argparse import Action
from gettext import find
import imp
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "/Users/hacked/Documents/projects/file-scraping/BookDAO/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.pdfdrive.com/")

book = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

search = driver.find_element_by_xpath('//*[@id="search-form"]')
#search.click()

time.sleep(5)
driver.quit()