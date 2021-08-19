from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input[placeholder='Enter first name']")
    first_name.send_keys("name")

    last_name = browser.find_element_by_css_selector("input[placeholder='Enter last name']")
    last_name.send_keys("ivanov")

    email = browser.find_element_by_css_selector("input[placeholder='Enter email']")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    text_file = browser.find_element_by_css_selector("input[id='file']")
    text_file.send_keys(os.path.join(current_dir, 'lesson22_step8.txt'))

    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
