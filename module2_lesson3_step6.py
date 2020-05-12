import math
import time
from selenium import webdriver

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_css_selector("button.trollface").click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	x = browser.find_element_by_id("input_value").text
	formula = str(math.log(abs(12*math.sin(int(x)))))

	text_area = browser.find_element_by_id("answer")
	text_area.send_keys(formula)

	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()
