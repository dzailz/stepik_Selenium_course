from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
time.sleep(5)
driver.get('http://suninjuly.github.io/math.html')
time.sleep(2)
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_id("robotCheckbox").click()
driver.find_element_by_id("robotsRule").click()
driver.find_element_by_css_selector(".btn").click()
