from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time
import math

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Считать значение для переменной x
    x_element = browser.find_element(By.CSS_SELECTOR,'label span:nth-child(2)')
    x = x_element.text

    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CLASS_NAME, 'form-control')
    y = calc(x)
    print(y)
    input1.send_keys(y)
    #Проскроллить страницу вниз.
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()

    # #Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    #Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    # Нажать на кнопку Submit
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
