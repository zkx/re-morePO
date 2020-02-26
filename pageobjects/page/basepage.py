#新增一个basepage文件
#base_page:完成一个类，对通用代码的一个引入，对__init__做一个封装，被其他需要__init__的PO类来调用
#让所有的子类继承BasePage
import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    #给driver增加一个类型，为WebDriver，不然为None类型的话就无法使用webdriver的方法，所以导入了from selenium.webdriver.remote.webdriver import WebDriver
    def __init__(self,driver:WebDriver=None):
        #index页面始终是从外面传的driver,按照PO原则，不想让这些内容污染case
        #basepage页面else有什么意义？ 查看#1和#2
        if driver == None:   # #1index没有driver，所以需要创建
            self.driver = webdriver.Chrome()
            #self.driver.get("https://work.weixin.qq.com/")
            #对访问地址进行自定义操作,让PO类可以自定义地址  变量名称前加_ 表示的是私有化变量
            self.driver.get(self._base_url)

            self.driver.implicitly_wait(3)
        else:        # #2register 和 login 已经有了driver，所以直接赋值就可以了
            self.driver=driver

    def close(self,sleeptime=10):
        time.sleep(sleeptime)
        self.driver.quit()   #第12行代码增加WebDriver类型，供driver使用quit方法
