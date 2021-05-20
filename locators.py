from selenium.webdriver.common.by import By


class Elements:
    username = (By.XPATH, '//input[@type="email"]')
    password = (By.XPATH, '//input[@type="password"]')
    login = (By.XPATH, '//span[@class="bk179 bk180 bk193"]')
    devices = (By.XPATH, '//*[@id="devices__tab"]/span/span[3]')
    router_ovrc_device = (By.XPATH, "//section[@id='root']/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr/td[4]/span")
    router_settings = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk367']/div/div[@class='bk541 bk540']/div[@class='bk543']/div/table/tbody/tr[1]/td[3]")
    router_configure = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[2]/span[1]/span[3]")
    port_settings = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]")
    back_router = (By.XPATH, "//span[@class='bk212 icon-arrow-left']")
    cancel_btn = (By.XPATH, "//button[@type='button']//span[@class='bk232 bk233 bk238']")
    port_forwarding_rules = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]")
    wan_settings = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/a[1]/span[1]/span[2]")
    content_filtering = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/a[1]/span[1]/span[2]")
    cf_cancel = (By.CSS_SELECTOR, "div.bk200.customerListOpen:nth-child(2) div.bk202 div.bk203 div.bk346 div.bk347 div.pageContent.bk4633.bk4624 div.pageContent__footer.bk4637 form.bk4670.bk4625 div.Footer__content.bk4671 div.bk4672:nth-child(2) div.Button.bk321.bk325.bk337.bk344:nth-child(1) button.Button__tag.bk322 > span.bk232.bk233.bk238")
    time_settings = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/a[1]/span[1]/span[2]")
    network_port_scans = (By.XPATH, "/html[1]/body[1]/section[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/a[1]/span[1]/span[2]")
    ovrc_email = 'jpdsauto@gmail.com'
    ovrc_password = 'SnapAV704'
