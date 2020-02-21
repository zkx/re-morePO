

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_test.page.index import Index


class TestIndex:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)

    def testRegister(self):
        #self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        index = Index(self.driver)  #这里的driver给到index时初始化使用
        index.goto_register().register("维尼")
        #注册详情页面
        #self.driver.find_element(By.ID,'corp_name').send_keys("维尼")
        #self.driver.find_element(By.ID,'submit_btn').click()
        #一个是首页，一个是注册详情页面，所以我们在写PO时，要有俩个页面
