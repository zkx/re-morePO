#企业微信首页
from selenium.webdriver.common.by import By

from pageobjects.page.basepage import BasePage
from pageobjects.page.login import Login
from pageobjects.page.register import Register

#BasePage类对通用代码的一个引入，对__init__做一个封装，被其他需要__init__的PO类来调用
#让所有的子类继承BasePage


class Index(BasePage):
    #对访问地址进行自定义操作
    _base_url = "https://work.weixin.qq.com/"
    '''

        #这里不是使用setup_method方法，而是初始化方法，注意初始化方法和setup_method方法区别
    def __init__(self,driver=None):
        #index页面始终是从外面传的driver,按照PO原则，不想让这些内容污染case
        if driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/")
            self.driver.implicitly_wait(3)
        else:
            self.driver=driver

    '''

    def goto_register(self):
        #这里的driver需要从外面传递过来，所以需要有一个接收driver的地方
        self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        return Register(self.driver) #这里的driver给到register时初始化使用

    def goto_login(self):
        self.driver.find_element(By.LINK_TEXT,'企业登录').click()
        return Login(self.driver)