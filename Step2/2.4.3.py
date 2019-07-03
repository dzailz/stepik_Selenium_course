from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
browser.implicitly_wait(5)
browser.find_element_by_css_selector(".btn").click()
message = browser.find_element_by_id("check_message")
assert "успешно" in message.text
