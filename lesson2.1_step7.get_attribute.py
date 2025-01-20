from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #Открыть страницу 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Считать значение для переменной x
    x_element = browser.find_element(By.ID,'treasure')
    x_element_1 = x_element.get_attribute("valuex")
    x = x_element_1
    print(x)
    
    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, 'answer')
    y = calc(x)
    print(y)
    input1.send_keys(y)
    
    #Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    
    #Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "div button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    