import time

import requests
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1080,720")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--allow-insecure-localhost")
chrome_options.add_argument("--headless")

driver = webdriver.Remote(
    command_executor="https://standalone-chrome-30300274673.asia-east1.run.app/wd/hub",
    options=chrome_options,
)

driver.get("https://www.ptt.cc/bbs/index.html")

time.sleep(10)

# //*[@id="main-container"]/div[2]/div[2]/a
# /html/body/div[2]/div[2]/div[2]/a
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/form/div[1]/button").click()

print(driver.get_cookies())
# Each cookie_dict be like: {'domain': 'www.ptt.cc', 'httpOnly': False, 'name': 'over18', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}
cookies = {cookie_dict["name"]: cookie_dict["value"] for cookie_dict in driver.get_cookies()}

res = requests.get(
    "https://www.ptt.cc/bbs/Gossiping/index.html",
    cookies=cookies,
)

print(res.text)

time.sleep(120)
