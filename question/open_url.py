# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: open_url
# Author: xiaxu
# DATA: 2023/3/25
# Description:
# ---------------------------------------------------
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://www.baidu.com'
driver = webdriver.Firefox()
try:
    driver.get(url)
    driver.maximize_window()
    print(driver.get_cookies())
    driver.delete_all_cookies()
    print('after delete_all_cookies:',driver.get_cookies())
    driver.refresh()
    print(driver.window_handles)
    print(driver.current_window_handle)
    print(driver.current_url)
    print(driver.find_elements(By.ID,'u1'))
except:
    pass
finally:
    time.sleep(5)
    driver.quit()