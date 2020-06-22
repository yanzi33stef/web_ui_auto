#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-04-05 14:34
# @Author   :  Ella

login_error_msg = [
    {"account": "", "pwd": "123456", "expected": "账号不能为空"},
    {"account": "1", "pwd": "123456", "expected": "用户不存在"},
    {"account": "18510289845", "pwd": "", "expected": "密码不能为空"},
    {"account": "18510289845", "pwd": "123", "expected": "密码有效长度是6到30个字符"},
]

login_success = [
    {"account": "18510289845", "pwd": "qwer1234", "expected": "北京-臭臭-24期"}
]

