from selenium import webdriver
from math import log, sin
import time


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


driver = webdriver.Chrome()
time.sleep(2)
driver.get('http://suninjuly.github.io/get_attribute.html')
time.sleep(2)
y = calc(driver.find_element_by_id('treasure').get_attribute('valuex'))
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_id("robotCheckbox").click()
driver.find_element_by_id("robotsRule").click()
driver.find_element_by_css_selector(".btn").click()

