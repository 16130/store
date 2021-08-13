class Hkrdata:


    #登陆成功的用例数据
    login_succeed_data = [
        {"username":"root","password":"root","expect":"Student Login"}
    ]

    #登陆密码错误的用例数据:@id='msg_uname'
    login_pwd_error_data = [
        {"username":"root","password":"qwe","expect":"账户名错误或密码错误!别瞎弄!"}
    ]

    #登陆用户名错误的用例数据
    login_un_error_data = [
        {"username":"qwr","password":"root","expect":"账户名错误或密码错误!别瞎弄!"}
    ]

    #进入修改头像界面的数据
    alter_portrait_init = [
        {"username":"root","password":"root","expect":"头像"}
    ]







