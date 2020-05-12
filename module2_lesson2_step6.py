import time
from selenium import webdriver
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element_by_id("input_value").text
	x_answer = calc(x)

	browser.execute_script("window.scrollBy(0, 100);")

	text_area = browser.find_element_by_id("answer")
	text_area.send_keys(str(x_answer))

	checkbox = browser.find_element_by_id("robotCheckbox").click()
	radio = browser.find_element_by_id("robotsRule").click()
	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()
