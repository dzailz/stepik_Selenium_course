from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
driver.get('https://suninjuly.github.io/execute_script.html')
x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
driver.find_element_by_id("answer").send_keys(y)
driver.find_element_by_id("robotCheckbox").click()
button = driver.find_element_by_css_selector(".btn")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
driver.find_element_by_id("robotsRule").click()
button.click()
