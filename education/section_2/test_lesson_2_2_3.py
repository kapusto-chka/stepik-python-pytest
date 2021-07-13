# import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    x = int(num1) + int(num2)

    browser.find_element(By.CSS_SELECTOR, '.custom-select').click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x))


    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
