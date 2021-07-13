import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = a.get_attribute('valuex')

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

    button = browser.find_element_by_css_selector(".btn.btn-default").click()

finally:
    time.sleep(10)
    browser.quit()
