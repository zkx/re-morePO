from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testerhome.com/")
driver.find_element_by_link_text('社团').click()
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@data-name="霍格沃兹测试学院"]').click()
driver.implicitly_wait(10)
#driver.find_element_by_xpath('//*[@href="/topics/22195"]').click()
driver.find_element_by_partial_link_text('测开 11 期_企业微信 web 自动化实战').click()


