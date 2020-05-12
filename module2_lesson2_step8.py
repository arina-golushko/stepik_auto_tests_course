import os
import time
from selenium import webdriver

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_name("firstname").send_keys("Arina")
	input2 = browser.find_element_by_name("lastname").send_keys("Golushko")
	input3 = browser.find_element_by_name("email").send_keys("arinka@")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'test.txt')
	uploaded_file = browser.find_element_by_id("file").send_keys(file_path)

	button = browser.find_element_by_css_selector("button.btn").click()

finally:
	time.sleep(10)
	browser.quit()
