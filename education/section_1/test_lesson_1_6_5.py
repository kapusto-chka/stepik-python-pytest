import math
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


link = "http://suninjuly.github.io/find_link_text"


link


try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_2 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="first_name"]').send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, '.form-control[name="last_name"]').send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city').send_keys("Smolensk")

    input4 = browser.find_element(By.CSS_SELECTOR, '#country').send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


