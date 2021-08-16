#encoding=utf-8
from appium import webdriver
import time


#Appium Server,端口号默认为4723
server = "http://localhost:4723/wd/hub"

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "deviceName": "127.0.0.1:62001",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}

#链接手机和app
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(5)


i = 0
while i < 5:
    time.sleep(10)
    start_x = 350
    start_y = 926
    stop_x = 350
    stop_y = 200
    driver.swipe(start_x,start_y,stop_x,stop_y)
    i = i + 1



driver.quit()

