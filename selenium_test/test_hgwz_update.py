import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHgwz:

    #需手动打出,无提示
    def setup_method(self):
        self.driver = webdriver.Chrome()
        #导航的方法 包括前进、后退，首先学习的是get
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)

    def wait(self,time,method):
        #todo
        #试试return
        waite = WebDriverWait(self.driver,time).until(method)
        return waite

    def test_hogwards(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        #显示等待
        #todo
        #可以理解为日程
        #time.sleep(3) 这不是显式等待哦
        element = (By.LINK_TEXT,'霍格沃兹测试学院') #element定义一个元组，提供给expected_conditions和find_element使用
        #显式等待  WebDriverWait  expected_conditions里面已经有了很多我们需要满足的条件,初始化需要给一个定位符locator(当满足某个状态时，例如可不可以点击，才来帮我们查找)，此时需要导入expected_conditions类
        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
        self.wait(10,expected_conditions.element_to_be_clickable(element)) #采取一个简单的方法封装后调用
        #self.driver.find_element(By.LINK_TEXT,'霍格沃兹测试学院').click()
        self.driver.find_element(*element).click()  #和28行的数据一样，此时为元组，元组拆箱 本来要传俩个元素，我们用*元组，将俩个元素拆开
        #隐式等待
        #todo
        #self.driver.implicitly_wait(5)
        element2=(By.CSS_SELECTOR,'.topics .topic:nth-child(1) .title a')
        self.wait(10,expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()

        #self.wait(10,lambda x:len(self.driver.window_handles>1))

    # 需手动打出,无提示
    #def teardown(self):
    #    time.sleep(3)
    #    self.driver.quit()


