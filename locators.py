from selenium.webdriver.common.by import By


class Elements:
    username = (By.XPATH, '//input[@type="email"]')
    password = (By.XPATH, '//input[@type="password"]')
    login = (By.XPATH, '//span[@class="bk179 bk180 bk193"]')
    devices = (By.XPATH, '//a[@id="devices__tab"]//span[@class="bk564 bk567"]//span[@class="bk232 bk233 bk238"]')
    router_ovrc_device = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk346']/div[@class='bk347']/div[@class='bk485']/div/div[@class='bk870 bk869']/div[@class='bk872']/div/table/tbody/tr[1]/td[3]")
    router_settings = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk367']/div/div[@class='bk541 bk540']/div[@class='bk543']/div/table/tbody/tr[1]/td[3]")
    router_configure = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk621']/div[@class='bk717']/div[@class='']/div[@class='bk720']/div[@class='bk721 bk725']/a[2]/span[1]/span[3]")
    port_settings = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk1154']/div[@class='bk1208']/div[@class='']/div/div[@class='bk1207']/div[1]/div[1]/div[1]/a[1]/span[1]/span[2]")
    back_router = (By.XPATH, "//span[@class='bk212 icon-arrow-left']")
    port_forwarding_rules = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk1751']/div[@class='bk1805']/div[@class='']/div/div[@class='bk1804']/div[@class='bk1848']/div[@class='bk1849']/div[2]/a[1]/span[1]/span[2]")
    wan_settings = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk1751']/div[@class='bk1805']/div[@class='']/div/div[@class='bk1804']/div[@class='bk1848']/div[@class='bk1849']/div[3]/a[1]/span[1]/span[2]")
    content_filtering = (By.XPATH, "//div[@class='bk1871']//div[@class='bk1850']//a[@class='bk1868']//span//span[@class='bk232 bk233 bk238']")
    time_settings = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk1751']/div[@class='bk1805']/div[@class='']/div/div[@class='bk1804']/div[@class='bk1848']/div[@class='bk1849']/div[5]/a[1]/span[1]/span[2]")
    network_port_scans = (By.XPATH, "//body/section[@id='root']/div[@class='bk200 customerListOpen']/div[@class='bk202']/div[@class='bk203']/div[@class='bk249']/div[@class='bk250']/div[@class='bk1751']/div[@class='bk1805']/div[@class='']/div/div[@class='bk1804']/div[@class='bk1848']/div[@class='bk1849']/div[@class='bk1850']/a[@class='bk1868']/span/span[2]")
    ovrc_email = 'jpdsauto@gmail.com'
    ovrc_password = 'SnapAV704'
