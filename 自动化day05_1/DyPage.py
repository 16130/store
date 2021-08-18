import time

class DyPage:
    def __init__(self,drive):
        self.driver = drive  #将driver声明为全局变量

    def login(self):
        self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()

        i = 0
        while i < 5:
            time.sleep(6)
            start_x = 350
            start_y = 926
            stop_x = 350
            stop_y = 200
            self.driver.swipe(start_x, start_y, stop_x, stop_y, 300)
            i = i + 1








