class HkrPage:
    def __init__(self,drive):
        self.driver = drive  #将driver声明为全局变量

    def login(self,username,password):
        # 输入用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        # 点击登陆
        self.driver.find_element_by_xpath("//*[@id='submit']").click()


    def get_succes_data(self):
        return self.driver.title


    def get_error_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text

    def get_un_error_data(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text

    def portrait_init(self,username,password):
        # 输入用户名
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        # 输入密码
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        # 点击登陆
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        #点击修改头像
        self.driver.find_element_by_xpath("//*[@id='img']").click()


    def get_portrait_init(self):
        return self.driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[1]/span[1]").text