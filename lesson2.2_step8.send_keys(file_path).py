from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os

import time
import math

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Alexey")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div/input[2]")
    input2.send_keys("Tovstoles")
    input3 = browser.find_element(By.XPATH,"/ html / body / div / form / div / input[3]")
    input3.send_keys("al@mail.com")

    #Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    #Поиск нужного элемента на сайте
    element =  browser.find_element(By.ID, "file")
    #Загружаем файл
    element.send_keys(file_path)

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "div button")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
