import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_xpath_form")

try:
	input1 = browser.find_element_by_name("first_name")
	input1.send_keys("Arina")
	input2 = browser.find_element_by_name("last_name")
	input2.send_keys("Golushko")
	input3 = browser.find_element_by_class_name("city")
	input3.send_keys("Gomel")
	input4 = browser.find_element_by_id("country")
	input4.send_keys("Belarus")

	button = browser.find_element_by_xpath("//button[text()='Submit']")
	button.click()

finally:
	time.sleep(10)
	browser.quit()