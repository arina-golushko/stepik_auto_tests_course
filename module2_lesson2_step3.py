import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def sum(a, b):
	return a+b

try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	a = int(browser.find_element_by_css_selector("h2 #num1").text)
	b = int(browser.find_element_by_css_selector("h2 #num2").text)
	c = str(sum(a, b))

	dropdown = browser.find_element_by_tag_name("select").click()
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(c)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(15)
	browser.quit()
