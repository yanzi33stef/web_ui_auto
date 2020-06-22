#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-04-05 17:09
# @Author   :  Ella

import unittest
import time
from selenium import webdriver
from ddt import ddt, data
from pages.login_page import LoginPage
from pages.index_page import IndexPage
from data.index_data import course_code_error
from data.login_data import login_success


@ddt
class TestIndex(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        account = login_success[0]
        LoginPage(self.driver).login(account['account'], account['pwd'])

    @data(*course_code_error)
    def test_add_course_up_error(self, code):
        """测试加入课程失败：{}"""
        """
        1.进入首页
        2.点击加入课程按钮
        3.输入课程码
        4.点击加入
        """
        IndexPage(self.driver).add_course_up(code['course_code'])
        actual = IndexPage(self.driver).get_toast().text

        self.assertEqual(actual, code['expected'])

    @data(*course_code_error)
    def test_add_course_down_error(self, code):
        """测试加入课程失败：{}"""
        """
        1.进入首页
        2.点击加入课程按钮
        3.输入课程码
        4.点击加入
        """
        IndexPage(self.driver).add_course_down(code['course_code'])
        actual = IndexPage(self.driver).get_toast().text

        self.assertEqual(actual, code['expected'])


if __name__ == '__main__':
    unittest.main()
