from selenium import webdriver
import time

buttonLink = '//div[6]/button[3]'
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")

    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")

    button = browser.find_element_by_xpath(buttonLink)
    button.click()

finally:
    time.sleep(30)
    browser.quit()