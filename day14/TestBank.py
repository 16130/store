from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from Bank import Bank_addUser
from Bank import Bank_query
from Bank import Bank_store
from Bank import Bank_drawCash
from Bank import Bank_transferMoney



#数据源
#开户
adduser = [
    ["12345678","张三","123456","中国","北京","昌平","123","200015020","2021-08-06"]
]

#存钱
store = [
    ["62567789"]
]

#取钱
drawcash = [
    ["99054513","12345","10000"]
]

#转账
transfer = [
    ["62567789","99054513","123456","20000"]
]


#查询
query = [
    ["99054513","12345"]
]


@ddt  # 注解，注释这个类是参数化类
class Testbank(TestCase):

    #测试开户
    @data(*adduser)  #引入数据源
    @unpack

    def testAdd(self,account,username,password,country,province,street,gate,money,regiaterDate):
        #调用被测方法
        test_sdduser = Bank_addUser().bank_addUser(account,username,password,country,province,street,gate,money,
                                                   regiaterDate)

        #断言
        self.assertEqual(test_sdduser,1)



    #测试存钱
    @data(*store)
    @unpack

    def testSore(self,account):
        # 调用被测方法
        test_store = Bank_store().bank_store(account)

        #断言
        self.assertEqual(test_store, 0)


    #测试取钱
    @data(*drawcash)
    @unpack

    def testDraw(self,account, password, cash):
        #调用被测方法
        test_draw = Bank_drawCash().bank_drawCash(account, password, cash)

        #断言
        self.assertEqual(test_draw,0)


    #测试转账
    @data(*transfer)
    @unpack

    def testTransfer(self,cardNum, collection, in_password, amount):
        #调用被测方法
        test_transfer = Bank_transferMoney().bank_transferMoney(cardNum, collection, in_password, amount)

        #断言
        self.assertEqual(test_transfer,0)



    #测试查询
    @data(*query)
    @unpack

    def testQuery(self,account, password):
        #调用被测方法
        test_query = Bank_query().bank_query(account, password)

        #断言
        self.assertEqual(test_query,0)






