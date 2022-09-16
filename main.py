import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
options.page_load_strategy = 'eager'

disableInfoBar = ['enable-automation']
options.add_experimental_option('excludeSwitches', disableInfoBar)

driver = webdriver.Chrome(options=options)
driver.get("https://www.mobile.de/")

# Waits 10 seconds to DOM complete and two seconds more to not act fast
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button').click()
time.sleep(10)
