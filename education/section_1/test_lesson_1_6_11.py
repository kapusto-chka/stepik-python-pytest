# внутри написал условие, по которому будет определяться ссылка (на норм страницу и страницу с багом)
# нужно ввеести цифру 1 или 2 на первом этапе 1 - откроется страница без бага; 2 - откроется страница с багом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'

x = int(input('Введите число 1 или 2: '))

if x == 1:
    browser = webdriver.Chrome().get(link_1)
elif x == 2:
    browser = webdriver.Chrome().get(link_2)
else:
    print('вы не справились')
    exit()
try:
    input1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]').send_keys('Ivan')
    input2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]').send_keys('Ivanov')
    input3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('i.ivanov@testmail.com')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
