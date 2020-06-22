#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     :  2020-05-12 14:56
# @Author   :  Ella

import os
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd()}

options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://pypi.org/project/selenium/#files')
driver.find_element_by_link_text('selenium-3.141.0.tar.gz').click()

time.sleep(5)

