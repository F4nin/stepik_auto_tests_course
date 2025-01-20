from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os

import time
import math

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем на кнопку
    input1 = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()

    #Переключение на окно с alert и его подтвержение
    alert = browser.switch_to.alert
    alert.accept()

    # Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, 'label span:nth-child(2)')
    x = x_element.text
    print(x)

    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    y = calc(x)
    print(y)
    input1.send_keys(y)

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "div button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
