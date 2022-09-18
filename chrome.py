import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait

import random

class SearchAgent:
    driver = None
    loadingURL = None
    sucess = 0
    targetList = []

    def __init__(self, loadingURL: str):
        print('Initing!')
        self.loadingURL = loadingURL
        options = Options()
        options.page_load_strategy = 'eager'
        disableInfoBar = ['enable-automation']
        options.add_experimental_option('excludeSwitches', disableInfoBar)
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.53 Safari/537.36'})
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.delete_cache()
        self.driver.get(self.loadingURL)
        self.checkCookie()
        self.driver.get(loadingURL)
        self.checkCookie()

    def delete_cache(self):
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        self.driver.get('chrome://settings/clearBrowserData')  # for old chromedriver versions use cleardriverData
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
        actions.perform()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
        actions.perform()
        time.sleep(5)  # wait some time to finish
        self.driver.close()  # close this tab
        self.driver.switch_to.window(self.driver.window_handles[0])  # switch back

    def eraseCache(self):
        self.driver.execute_script("window.localStorage.clear()")
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.delete_cache()

    def loadSiteOnNewTab(self, url: str):
        self.driver.execute_script("window.open('');")
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.get(url)

    def returnMainTab(self):
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def checkCookie(self):
        time.sleep(7)
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button').click()
        except:
            print("I did not find any cookie :>")

    def checkPageSize(self) -> int:
        time.sleep(10)
        pageElement = self.driver.find_element(By.CLASS_NAME, 'pagination')
        links = list(pageElement.find_elements(By.TAG_NAME, "li"))
        pageSize = int(
            links[-2].get_attribute("innerHTML").split("data-touch=\"link\"", maxsplit=1)[0].rsplit("\"", 1)[0].split(
                "Seite ", maxsplit=2)[1])
        print(f'Active pages: {pageSize}')
        return pageSize

    def listCars(self):
        self.targetList = []
        self.driver.implicitly_wait(10)
        time.sleep(2)
        elements = list(self.driver.find_elements(By.XPATH, '//a[@href]'))
        print(f'Loaded elements : {len(elements)}')

        for x in elements:
            if x.get_attribute("href").find("action=eyeCatcher") != -1:
                self.targetList.append(x.get_attribute("href"))

        print(f'Filtered : {len(self.targetList)}')

    def writeMail(self):
        msgbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=\"vip-contact-form\"]/div/div[1]/textarea")))
        msgbox.clear()
        print("Passed!")
        time.sleep(2)
        msgbox.send_keys("a")
        time.sleep(2)
        nameTxtBox = self.driver.find_element(By.XPATH, "//*[@id=\"vip-contact-form\"]/div/div[2]/div[1]/div/div/input")
        nameTxtBox.clear()
        nameTxtBox.send_keys("b")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, "//*[@id=\"contact-type-email-section\"]/div/div/input")
        email.clear()
        email.send_keys("yigityilmaz1923@hotmail.com")

    def sendMails(self):
        print("Sending Mails!")
        page = 1
        for y in range(1, 51):
            self.eraseCache()
            self.loadSiteOnNewTab(f"https://suchen.mobile.de/fahrzeuge/search.html?adLimitation=ONLY_FSBO_ADS"
                                  f"&damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1"
                                  f".makeId=1900&makeModelVariant1.modelId=9&pageNumber="
                                  f"{y}&ref=srpPreviousPage&scopeId=C&sortOption.sortBy=relevance&refId=23bbd1ef-2fa1"
                                  f"-4123-ab94-2d4af888c843")
            self.checkCookie()
            self.listCars()
            for x in self.targetList:
                ratio = (self.sucess / page)
                print(f'Success rate : {ratio}*100')
                self.driver.execute_script("window.localStorage.clear()")
                self.driver.delete_all_cookies()
                self.driver.set_window_size(random.randint(512, 1024), random.randint(512, 1920))
                time.sleep(2)
                print(f'Entering page : {page}')
                print(x)
                self.loadSiteOnNewTab(x)
                self.checkCookie()
                try:
                    self.writeMail()
                    self.sucess += 1
                except:
                    print("The car has been closed :<")
                self.returnMainTab()
                page += 1
            self.returnMainTab()
