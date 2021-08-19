from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)

    call_alert = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    call_alert.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_value = browser.find_element_by_css_selector("span[id='input_value']").text
    y = calc(x_value)

    answer = browser.find_element_by_css_selector("input[id='answer']")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("button[class='btn btn-primary']")
    button.click()


finally:
    time.sleep(20)
    browser.quit()
