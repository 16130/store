from selenium import webdriver
import time

#创建驱动
driver = webdriver.Chrome()
#打开网址
driver.get("http://localhost:8080/HKR")
driver.maximize_window()  #最大化

#1.输入用户名
driver.find_element_by_id("loginname").send_keys("root")
#2.输入密码
driver.find_element_by_id("password").send_keys("root")
#3.登陆
driver.find_element_by_id("submit").click()
#4.点击头像
driver.find_element_by_id("img").click()
time.sleep(1)
#5.更换头像
driver.find_element_by_xpath("//*[@id='ul_pic']/li[4]").click()
time.sleep(1)
#6.关闭修改头像选项卡
driver.find_element_by_xpath("//*[@href='javascript:;' and @class='tabs-close']").click()
time.sleep(1)
driver.refresh()   #刷新界面
#7.选择培训时间
driver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9（上晚自习）")
# #8.选择授课讲师
driver.find_element_by_xpath("//*[@name='teaName' and @class='show_tea']").send_keys("贾生")
# #9.评价内容
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()
driver.find_element_by_xpath("//*[@id='textarea']").send_keys("无")
driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()
#8.点击修改个人信息
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
time.sleep(1)
#8.1清空输入框
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("root")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("root")

driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").clear()
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("28")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("男")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys("河北")


driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys("13552648187@qq.com")

driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").clear()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("无")


driver.find_element_by_xpath("//*[@id='btn_modify']").click()    #点击修改
#8.2关闭修改信息选项卡
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()

#9.查看所有好友
driver.find_element_by_xpath("//*[@id='_easyui_tree_10']/span[4]/a").click()
#9.1关闭好友选项卡
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()






time.sleep(3)
driver.quit()

