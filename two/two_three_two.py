import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('[type=submit]')
    time.sleep(2)
    input1.click()

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    options2 = browser.find_element_by_css_selector('#answer').send_keys(y)
    input2 = browser.find_element_by_css_selector('[type=submit]')
    input2.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла