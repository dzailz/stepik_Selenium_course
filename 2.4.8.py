from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Selenium_Calc import calc

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
browser.find_element_by_id("book").click()
x = browser.find_element_by_id("input_value").text
browser.find_element_by_id("answer").send_keys(calc(x))
browser.find_element_by_id("solve").click()

"""
# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
"""
