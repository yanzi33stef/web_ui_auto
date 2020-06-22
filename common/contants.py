#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-06-20 22:09
# @Author   :  Ella
import os

# 项目目录的路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 测试用例模块所在目录
CASE_DIR = os.path.join(BASE_DIR, "testcases")

# 测试报告的路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")
