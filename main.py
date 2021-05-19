import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Elements
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options=Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile

driver = webdriver.Firefox(firefox_profile=firefox_profile, options=options)
driver.implicitly_wait(10)

driver.get('https://app.ovrc.com/')

un = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.username))
un.send_keys(*Elements.username)

pw = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.password))
pw.send_keys(*Elements.password)

login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.login))
login.click()

devices = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.devices))
devices.click()

router = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.router_ovrc_device))
router.click()

router_configure = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.router_configure))
router_configure.click()

router_port_config = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.port_settings))
router_port_config.click()

router_back = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.back_router))
router_back.click()

router_port_forward = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.port_forwarding_rules))
router_port_forward.click()

driver.quit()

