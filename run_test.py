#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-04-05 20:24
# @Author   :  Ella
import unittest
import os
import time
from common.contants import CASE_DIR, REPORT_DIR
from library.HTMLTestRunnerNew import HTMLTestRunner

now_time = time.strftime("%Y-%m-%d %H_%M_%S")

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二步：加载测试用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

# 第三步：创建一个测试用例运行程序
report_path = os.path.join(REPORT_DIR, "report.html")

with open(report_path, "wb") as f:
    runner = HTMLTestRunner(stream=f,
                            title="测试报告",
                            description="测试报告的描述信息",
                            verbosity=2,
                            retry=2
                            )
    # 运行测试套件
    runner.run(suite)
