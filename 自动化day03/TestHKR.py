from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from Hkrdata import Hkrdata #页面数据
from HkrPage import HkrPage #页面的操作逻辑
import time

@ddt
class TestLogin(TestCase):
    #在每个操作之前先做预备工作
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/HKR")
        time.sleep(2)

    #在每个用例执行之后，将浏览器关闭
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    #登陆成功用力
    @data(*Hkrdata.login_succeed_data)
    def testLoginsuccess(self,testdata):
    #提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = HkrPage(self.driver)
        login.login(username,password)

        #获取实际结果
        result = login.get_succes_data()

        #断言
        self.assertEqual(expect,result)


    #登陆失败用例
    @data(*Hkrdata.login_pwd_error_data)
    def testLoginerror(self, testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = HkrPage(self.driver)
        login.login(username, password)

        #  获取实际结果
        result = login.get_error_data()
        # 断言
        self.assertEqual(expect, result)

    @data(*Hkrdata.login_un_error_data)
    def testLogin_un_error(self,testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = HkrPage(self.driver)
        login.login(username, password)

        #  获取实际结果
        result = login.get_error_data()
        # 断言
        self.assertEqual(expect, result)


    @data(*Hkrdata.alter_portrait_init)
    def testalter_portrait(self,testdata):
        # 提取用户名，密码，期望结果
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        login = HkrPage(self.driver)
        login.portrait_init(username, password)

        #  获取实际结果
        result = login.get_portrait_init()

        if result == expect:
            print("用例执行成功！")
        else:
            print("用例执行失败！")
            self.driver.save_screenshot("login1.jpg")

