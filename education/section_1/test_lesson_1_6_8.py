import time
from selenium.webdriver.common.by import By
from selenium import webdriver


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="last_name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
