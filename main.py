import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


targetList = []
def delete_cache():
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData')  # for old chromedriver versions use cleardriverData
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
    actions.perform()
    time.sleep(5)  # wait some time to finish
    driver.close()  # close this tab
    driver.switch_to.window(driver.window_handles[0])  # switch back


options = Options()
options.page_load_strategy = 'eager'

ua = UserAgent()
userAgent = ua.random

disableInfoBar = ['enable-automation']
options.add_experimental_option('excludeSwitches', disableInfoBar)
options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(options=options)

# Cache eraser
driver.delete_all_cookies()
time.sleep(2)
delete_cache()


# Waits 10 seconds to DOM complete and two seconds more to not act fast
driver.get("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&ms=1900%3B9%3B%3B%3B&ref=dsp&s=Car&sb=rel&st=FSBO&vc=Car")

time.sleep(7)

try:
    driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button').click()
except:
    print("I did not find any cookie :>")

driver.implicitly_wait(10)
time.sleep(2)
elements = list(driver.find_elements(By.XPATH, '//a[@href]'))
print(f'Loaded elements : {len(elements)}')

for x in elements:
    if x.get_attribute("href").find("action=eyeCatcher") != -1:
        targetList.append(x.get_attribute("href"))

print(f'Filtered : {len(targetList)}')

for x in targetList:
    print(x)

time.sleep(10)
driver.quit()
