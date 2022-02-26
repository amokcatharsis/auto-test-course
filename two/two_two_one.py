import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def sum(x, y):
    return str(x + y)

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    y_element = browser.find_element_by_id('num2')
    x = int(x_element.text)
    y = int(y_element.text)
    z = sum(x, y)

    browser.find_element_by_css_selector('#dropdown').click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)  # ищем элемент с текстом "z"

    browser.find_element_by_css_selector("[type=submit]").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла