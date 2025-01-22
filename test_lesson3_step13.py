from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class TestAbs(unittest.TestCase):
    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(1) input")
        input1.send_keys("Alexey")
        input2 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(2) input")
        input2.send_keys("Tovstoles")
        input3 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(3) input")
        input3.send_keys("1@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "div button")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Текст не совпадает с тем что должно быть/или его нет')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(1) input")
        input1.send_keys("Alexey")
        input2 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(2) input")
        input2.send_keys("Tovstoles")
        input3 = browser.find_element(By.CSS_SELECTOR, "html body div form div:nth-child(1) div:nth-child(3) input")
        input3.send_keys("1@mail.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "div button")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Текст не совпадает с тем что должно быть/или его нет')

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()        

if __name__ == "__main__":
    pytest.main()
