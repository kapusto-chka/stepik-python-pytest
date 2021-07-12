import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()





    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    # time.sleep(2)
    # welcome_text_elt = browser.find_element_by_tag_name("h1")
    # welcome_text = welcome_text_elt.text
    #
    # assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
