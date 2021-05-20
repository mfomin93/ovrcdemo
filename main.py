import time
import logging
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Elements
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.implicitly_wait(10)

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='a')


def wait_for_correct_current_url(url):
    WebDriverWait.until(
        lambda driver: driver.current_url == url)


def back_button():
    back = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.back_router))
    back.click()
    logging.info('Back Button PRESSED')


loop_counter = 100
options = Options()
capabilities = DesiredCapabilities.CHROME
capabilities["pageLoadStrategy"] = "normal"

for x in range(0, int(loop_counter)):
    logging.info('Automated script started!')

    driver.maximize_window()
    logging.info('Window MAXIMIZED')
    url = 'https://app.ovrc.com/'
    driver.get(url)
    # WebDriverWait(driver, 10).until(EC.url_changes(changed_url))
    logging.info('Navigating to OVRC Web Page')

    un = WebDriverWait(driver, 60).until(EC.visibility_of_element_located(Elements.username))
    logging.info(un)
    un.send_keys(*Elements.ovrc_email)
    logging.info('Entered USERNAME')

    pw = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.password))
    logging.info(pw)
    pw.send_keys(*Elements.ovrc_password)
    logging.info('Entered PASSWORD')

    login = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.login))
    logging.info(login)
    login.click()
    logging.info('Login button PRESSED')
    devices = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.devices))
    logging.info(devices)
    devices.click()
    logging.info('Device List Selected')

    router = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.router_ovrc_device))
    logging.info(router)
    router.click()
    logging.info('ROUTER device selected.')

    router_configure = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.router_configure))
    logging.info(router_configure)
    router_configure.click()
    logging.info('Router CONFIGURATION selected.')

    router_port_config = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.port_settings))
    logging.info(router_port_config)
    router_port_config.click()
    time.sleep(1)
    logging.info('Selecting PORT SETTINGS')
    back_button()

    router_port_forward = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Elements.port_forwarding_rules))
    logging.info(router_port_forward)
    router_port_forward.click()
    logging.info('PORT FORWARDING menu selected.')
    time.sleep(1)

    back_button()

    router_wan = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.wan_settings))
    logging.info(router_wan)
    router_wan.click()
    logging.info('WAN settings selected.')
    time.sleep(1)

    back_button()

    time_settings = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.time_settings))
    logging.info(time_settings)
    time_settings.click()
    logging.info('Checking TIME SETTINGS menu.')
    time.sleep(1)
    back_button()

    network_scans = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.network_port_scans))
    logging.info(network_scans)
    network_scans.click()
    logging.info('NETWORK PORT SCANS menu selected.')
    time.sleep(1)

    NS_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Elements.cancel_btn))
    logging.info(NS_button)
    NS_button.click()
    logging.info('CANCEL button selected.')
    time.sleep(1)
    logging.info('Restarting BROWSER and TEST!!!')
    driver.close()
    driver.start_session(capabilities=capabilities)

driver.quit()
