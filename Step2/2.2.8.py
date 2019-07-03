from selenium import webdriver
import os

with open('resume.txt', 'w') as file:
    file.write("Hello Selenium!!!")
pth = os.path.abspath("resume.txt")
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")
firstname = "Ivan"
lastname = "Ivanov"
email = "Ivanov.Ivan@gmail.com"

browser.find_element_by_name("firstname").send_keys(firstname)
browser.find_element_by_name("lastname").send_keys(lastname)
browser.find_element_by_name("email").send_keys(email)
browser.find_element_by_css_selector("#file").send_keys(pth)
browser.find_element_by_css_selector(".btn").click()