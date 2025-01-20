from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # посчитать сумму заданных чисел
    first_element = browser.find_element(By.ID, 'num1')
    second_element = browser.find_element(By.ID, 'num2')
    value_first_element = int(first_element.text)
    value_second_element = int(second_element.text)
    result = str(value_first_element + value_second_element)
    print(result)
    #Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(result)

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "div button")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

