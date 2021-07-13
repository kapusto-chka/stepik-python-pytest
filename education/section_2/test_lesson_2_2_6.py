# from selenium import webdriver
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value')
    x = x_element.text
    y = calc(x)


    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(calc(x))

    option1 = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()


    option2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')          # скролить пока опция станет видимой
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()

    button = browser.find_element(By.TAG_NAME, "button")                    # скролить пока кнопка станет видимой
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
