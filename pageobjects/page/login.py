from selenium.webdriver.common.by import By

from pageobjects.page.basepage import BasePage
from pageobjects.page.register import Register


class Login(BasePage):

    def scan_qrcode(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT,'企业注册').click()
        return Register(self.driver)