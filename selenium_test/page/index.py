#企业微信首页
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_test.page.register import Register


class Index:

    #这里不是使用setup_method方法，而是初始化方法，注意初始化方法和setup_method方法区别
    def __init__(self,driver):
        self.driver = driver

    def goto_register(self):
        #这里的driver需要从外面传递过来，所以需要有一个接收driver的地方
        self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        return Register(self.driver) #这里的driver给到register时初始化使用