import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector("div.form-group #input_value")
	x = x_element.text
	y = calc(x)

	textarea = browser.find_element_by_id("answer")
	textarea.send_keys(y)

	checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
	checkbox.click()

	radio = browser.find_element_by_css_selector("[for='robotsRule']")
	radio.click()

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(10)
	browser.quit()
