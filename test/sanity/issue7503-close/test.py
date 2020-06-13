import time
import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from nw_util import *

def close_window(title):
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
        if title in driver.title:
            driver.find_element_by_id("close").click()
            break

def switch_to_window(title):
    for handle in driver.window_handles:
        driver.switch_to_window(handle)
        if title == driver.title:
            break

chrome_options = Options()
chrome_options.add_argument("nwapp=" + os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path=os.environ['CHROMEDRIVER'], chrome_options=chrome_options)
driver.implicitly_wait(5)

try:
    wait_window_handles(driver, 3)
    close_window("local file");
    close_window("Example");
    switch_to_window("main window")

    result_local = driver.find_element_by_id('result_local').get_attribute('innerHTML')
    result_remote = driver.find_element_by_id('result_remote').get_attribute('innerHTML')

    assert(result_local == "local")
    assert(result_remote == "remote")
finally:
    driver.quit()
