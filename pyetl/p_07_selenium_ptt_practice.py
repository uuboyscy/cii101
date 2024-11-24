import time

import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"/Users/uuboy.scy/side-project/tibame/cii101/pyetl/chromedriver")
driver = Chrome(service=service)

driver.get("https://www.ptt.cc/bbs/index.html")

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

# time.sleep(120)
