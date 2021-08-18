from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from ddt import unpack
from DyPage import DyPage #页面的操作逻辑
import time

@ddt
class TestLogin(TestCase):
    #在每个操作之前先做预备工作
    def setUp(self) -> None:
        # Appium Server,端口号默认为4723
        server = "http://localhost:4723/wd/hub"

        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
            "deviceName": "127.0.0.1:62001",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }

        # 链接手机和app
        self.driver = webdriver.Remote(server, desired_capabilities)
        time.sleep(15)

    #在每个用例执行之后，将浏览器关闭
    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()


    #登陆成功用力
    #@data(*Hkrdata.login_succeed_data)
    def testLoginsuccess(self,):


        login = DyPage(self.driver)
        login.login()





