#进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围。把代码贴到回复里。
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHomework2:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def testHomework(self):
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(6)
        self.driver.find_element(By.CSS_SELECTOR,'div.topic.media.topic-21805 .infos .title').click()


        #WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(By.TAG_NAME,'[data-toggle="dropdown"]'))
        #self.driver.find_element(By.TAG_NAME,'[data-toggle="dropdown"]').click()
        ele = (By.LINK_TEXT,'目录')
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(ele))
        self.driver.find_element(*ele).click()
        self.driver.switch_to.frame(0)
        self.driver.switch_to.window(self.driver.window_handles[1])

        time.sleep(5)
        self.driver.find_element_by_link_text('征集议题范围').click()

    def teardown(self):
        self.driver.implicitly_wait(5)
        self.driver.quit()