from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"D:\卢星宇\python自动化学习\day01\练习的html\练习的html\跳转页面\pop.html")
driver.maximize_window()  #窗口最大化

#点击链接
driver.find_element_by_id("goo").click()



time.sleep(3)
driver.quit()