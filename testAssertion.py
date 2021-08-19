from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name("first")
    input1.send_keys("name")

    input2 = browser.find_element_by_class_name("second")
    input2.send_keys("last")

    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("email")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
