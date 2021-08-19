from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    first_value = browser.find_element_by_css_selector("span[id='num1']").text
    second_value = browser.find_element_by_css_selector("span[id='num2']").text

    result = str(int(first_value) + int(second_value))

    select = Select(browser.find_element_by_css_selector("select[id='dropdown']"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button[class='btn btn-default']")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
