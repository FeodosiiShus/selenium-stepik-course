from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)
    x_value = browser.find_element_by_id("input_value").text
    y = calc(x_value)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for=robotCheckbox]")
    checkbox.click()

    radioButton = browser.find_element_by_css_selector("[for=robotsRule]")
    radioButton.click()

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
