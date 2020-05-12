import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	chest = browser.find_element_by_css_selector("img#treasure")
	chest_get_attribute = chest.get_attribute("valuex")

	x = chest_get_attribute
	y = calc(x)

	textarea = browser.find_element_by_id("answer")
	textarea.send_keys(y)

	checkbox = browser.find_element_by_id("robotCheckbox")
	checkbox.click()

	radio = browser.find_element_by_id("robotsRule")
	radio.click()

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

finally:
	time.sleep(5)
	browser.quit()
