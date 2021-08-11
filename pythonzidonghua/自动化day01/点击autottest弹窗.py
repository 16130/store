from selenium import webdriver
import time

driver = webdriver.Chrome()


driver.get(r"D:\卢星宇\python自动化学习\day01\练习的html\练习的html\上传文件和下拉列表\autotest.html")
driver.maximize_window()   #窗口最大化

#1.输入 用户名
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("张三")
#2.输入密码
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")
#3.下拉
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

#4.性别
driver.find_element_by_xpath("//*[@id='sexID1']").click()

#5.季节
driver.find_element_by_xpath("//*[@value='spring']").click()
driver.find_element_by_xpath("//*[@value='summer']").click()
driver.find_element_by_xpath("//*[@value='Auterm']").click()

#6.上传文件
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\卢星宇\python自动化学习\day01\无标题.png")

#7.点击弹窗
driver.find_element_by_xpath("//*[@id='buttonID']").click()

time.sleep(1)
driver.switch_to.alert.accept()



time.sleep(3)
driver.quit()




















