from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser.get(link)

    x_value = browser.find_element_by_css_selector("span[id='input_value']").text

    y = calc(x_value)

    answer = browser.find_element_by_css_selector("input[id='answer']")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("label[for='robotCheckbox']")
    checkbox.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    radioButton = browser.find_element_by_css_selector("input[id='robotsRule']")
    radioButton.click()

    button.click()

finally:
    time.sleep(20)
    browser.quit()
