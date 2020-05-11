import time
from selenium import webdriver

try:
	link = "http://suninjuly.github.io/registration1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input1 = browser.find_element_by_css_selector("div.first_block input.first")
	input1.send_keys("Arina")
	input2 = browser.find_element_by_css_selector("div.first_block input.second")
	input2.send_keys("Golushko")
	input3 = browser.find_element_by_css_selector("div.first_block input.third")
	input3.send_keys("arinka@mail")

	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	time.sleep(3)

	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text

	assert "Congratulations! You have successfully registered!" == welcome_text


finally:
	time.sleep(10)
	browser.quit()