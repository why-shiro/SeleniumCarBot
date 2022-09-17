import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait

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
driver.get(
    "https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&ms=1900%3B9%3B%3B%3B&ref=dsp&s=Car&sb=rel&st=FSBO&vc=Car")

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

pageElement = driver.find_element(By.CLASS_NAME, 'pagination')
links = list(pageElement.find_elements(By.TAG_NAME,"li"))
pageSize = int(links[-2].get_attribute("innerHTML").split("data-touch=\"link\"",maxsplit=1)[0].rsplit("\"",1)[0].split("Seite ",maxsplit=2)[1])
print(f'Active pages: {pageSize}')

page = 1
for x in targetList:
    time.sleep(2)
    driver.execute_script("window.localStorage.clear()")
    driver.delete_all_cookies()
    print(f'Entering page : {page}')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get(x)
    try:
        driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button').click()
    except:
        print("I did not find any cookie :>")
    msgbox = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id=\"vip-contact-form\"]/div/div[1]/textarea")))
    msgbox.clear()
    print("Passed!")
    time.sleep(2)
    msgbox.send_keys("a")
    time.sleep(2)
    nameTxtBox = driver.find_element(By.XPATH, "//*[@id=\"vip-contact-form\"]/div/div[2]/div[1]/div/div/input")
    nameTxtBox.clear()
    nameTxtBox.send_keys("b")
    time.sleep(2)
    email = driver.find_element(By.XPATH, "//*[@id=\"contact-type-email-section\"]/div/div/input")
    email.clear()
    email.send_keys("yigityilmaz1923@hotmail.com")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    page += 1

# https://suchen.mobile.de/fahrzeuge/search.html?adLimitation=ONLY_FSBO_ADS&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=1900&makeModelVariant1.modelId=9&pageNumber=2&ref=srpNextPage&scopeId=C&sortOption.sortBy=relevance&refId=4e7ec85b-0995-b068-5e53-98ef5d8661d7

time.sleep(10)
driver.quit()
