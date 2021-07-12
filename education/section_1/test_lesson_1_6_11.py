# внутри написал условие, по которому будет определяться ссылка (на норм страницу и страницу с багом)
# нужно ввеести цифру 1 или 2 на первом этапе 1 - откроется страница без бага; 2 - откроется страница с багом


from selenium import webdriver
import time

link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'
# x = int(input('Введите число 1 или 2: '))

# if x == 1:
#     browser = webdriver.Chrome()
#     browser.get(link_1)
# elif x == 2:
#     browser = webdriver.Chrome()
#     browser.get(link_2)
# else:
#     print('вы не справились')
#     exit()

try:
    browser = webdriver.Chrome()
    browser.get(link_1)
    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys("ivanpetrov@testmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()



try:
    browser = webdriver.Chrome()
    browser.get(link_2)
    input1 = browser.find_element_by_css_selector('.first_block .form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('.first_block .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('.first_block .form-control.third')
    input3.send_keys("ivanpetrov@testmail.com")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()