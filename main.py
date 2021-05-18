import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
from locators import Elements
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(15)

driver.get('https://app.ovrc.com/')
un = driver.find_element(*Elements.username)
un.send_keys(*Elements.username)
time.sleep(2)
pw = driver.find_element(*Elements.password)
pw.send_keys(*Elements.password)
time.sleep(2)
driver.find_element(*Elements.login).click()
time.sleep(3)
driver.quit()
