import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    price = WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book")
    if price:
        button.click()
        input_value = browser.find_element_by_id("input_value").text
        answer_value = calc(input_value)
        input_text = browser.find_element_by_id("answer")
        input_text.send_keys(answer_value)
        button_submit = browser.find_element_by_id("solve")
        button_submit.click()
finally:
    time.sleep(20)
    browser.quit()
