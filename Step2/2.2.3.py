from selenium import webdriver
from selenium.webdriver.support.ui import Select
browzer = webdriver.Chrome()
browzer.get("http://suninjuly.github.io/selects1.html")
num1 = int(browzer.find_element_by_id("num1").text)
num2 = int(browzer.find_element_by_id("num2").text)
otvet = str(num1 + num2)
select = Select(browzer.find_element_by_tag_name("select"))
select.select_by_value(otvet)
browzer.find_element_by_css_selector(".btn").click()