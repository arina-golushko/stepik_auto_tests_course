import math
import time
from selenium import webdriver

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button.btn").click()
	confirm = browser.switch_to.alert
	confirm.accept()

	x = browser.find_element_by_id("input_value").text
	formula = str(math.log(abs(12*math.sin(int(x)))))

	text_area = browser.find_element_by_id("answer")
	text_area.send_keys(formula)
	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()
