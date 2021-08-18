from HTMLTestRunner import HTMLTestRunner
import unittest
import os

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="这是一个抖音的测试报告",
    description="这是一个刷抖音的测试报告",
    verbosity=1,
    stream = open(file="抖音测试报告.html",mode="w+",encoding="utf-8")
)


runner.run(tests)
