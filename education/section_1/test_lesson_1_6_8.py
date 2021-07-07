import time
from selenium.webdriver.common.by import By
from selenium import webdriver


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="first_name"]').send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="last_name"]').send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city').send_keys("Smolensk")

    input4 = browser.find_element(By.CSS_SELECTOR, '#country').send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(15)
    browser.quit()
