#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-05-10 18:01
# @Author   :  Ella

from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')
driver.maximize_window()

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(5)

handles = driver.window_handles
print('当前窗口数为：{}'.format(len(handles)))
for i in handles:
    print(i)

driver.find_element_by_xpath("//a[contains(text(),'库的基本使用')]").click()

# t = driver.find_elements_by_xpath("//div[@class='result c-container ']/h3/a")
# print('搜索结果个数为：{}'.format(len(t)))
# num = random.randint(0, 3)
# t[num].click()

WebDriverWait(driver, 10).until(EC.new_window_is_opened(handles))
handles = driver.window_handles

print('当前窗口数为：{}'.format(len(handles)))
for j in handles:
    print(j)

driver.switch_to.window(handles[-1])
print(driver.title)

driver.find_element_by_xpath("//input[@type = 'search']").send_keys("1")
sleep(5)
driver.close()

driver.switch_to.window(handles[0])
print(driver.current_window_handle)
# driver.find_element_by_xpath("//a[contains(text(),'库的基本使用')]").click()
sleep(5)

driver.quit()
