"""
A long time ago in a galaxy far, far away...
Episode 2.3.6 A NEW WINDOW
"""

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element_by_css_selector(".btn").click()  # Yeah science, bi@#h!
new_window = browser.window_handles[1]
browser.switch_to_window(new_window)
x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_css_selector(".btn-primary").click()
