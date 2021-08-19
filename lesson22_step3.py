from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(link)

    img = browser.find_element_by_css_selector("img[src='images/chest.png']")
    value_x = img.get_attribute("valuex")

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(calc(value_x))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radioButton = browser.find_element_by_id("robotsRule")
    radioButton.click()

    button = browser.find_element_by_css_selector("button[type=submit]")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
