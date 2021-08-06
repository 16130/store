from HTMLTestRunner import HTMLTestRunner #运行器
import unittest

#1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\pythonProject1\day14",pattern="TestBank.py")

#2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份工商银行的测试报告",
    description = "这只是一份单元测试报告",
    verbosity = 1,
    stream = open("计算器.html",mode="w+",encoding="utf-8")
)

#3.运行所有用例
runner.run(tests)
