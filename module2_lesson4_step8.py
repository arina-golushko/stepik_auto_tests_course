import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	price = WebDriverWait(browser, 12). until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)

	browser.find_element(By.ID, "book").click()

	x = browser.find_element_by_id("input_value").text
	formula = str(math.log(abs(12*math.sin(int(x)))))

	text_area = browser.find_element_by_id("answer")
	text_area.send_keys(formula)
	button = browser.find_element_by_id("solve").click()

finally:
	time.sleep(10)
	browser.quit()
