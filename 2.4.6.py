from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/cats")
driver.find_element_by_id("button")