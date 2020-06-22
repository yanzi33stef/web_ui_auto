#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-04-04 22:01
# @Author   :  Ella
import logging
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_ele_visible(self, locator, timeout=30):
        """等待元素可见"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logging.error("等待元素超时")

    def wait_ele_presence(self, locator, timeout=30):
        """等待元素出现"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logging.error("等待元素超时")

    def move_to_ele(self, ele):
        """鼠标悬停"""
        action = ActionChains(self.driver)
        action.move_to_element(ele).perform()
