import pytest
import uuid
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import email, password


@pytest.fixture(scope="class", autouse="True")
def driver():
    driver = webdriver.Chrome()
    # max размер экрана
    driver.maximize_window()
    driver.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(email)
    time.sleep(3)  # небольшая задержка
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(password)
    time.sleep(3)  # небольшая задержка
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(3)  # небольшая задержка
    # # Проверяем, что мы оказались на главной странице пользователя
    # assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # time.sleep(3)  # небольшая задержка
    # driver.get('https://petfriends.skillfactory.ru/my_pets')
    # time.sleep(3)  # небольшая задержка

    yield driver

    driver.quit()

# @pytest.fixture()
# def my_pets():
#    # Вводим email
#    driver.find_element(By.ID, 'email').send_keys(email)
#    time.sleep(3)  # небольшая задержка
#    # Вводим пароль
#    driver.find_element(By.ID, 'pass').send_keys(password)
#    time.sleep(3)  # небольшая задержка
#    # Нажимаем на кнопку входа в аккаунт
#    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#    time.sleep(3)  # небольшая задержка
#    # Проверяем, что мы оказались на главной странице пользователя
#    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
#    time.sleep(3)  # небольшая задержка
#    driver.get('https://petfriends.skillfactory.ru/my_pets')
#    time.sleep(3)  # небольшая задержка

# @pytest.fixture
# def web_browser(request, driver):
#     browser = driver
#     browser.maximize_window()
#     # Вернуть объект браузера
#     yield browser
#     # Этот код выполнится после отрабатывания теста:
#     if request.node.rep_call.failed:
#         # Сделать скриншот, если тест провалится:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Создаем папку screenshots и кладем туда скриншот с генерированным именем:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # Для дебагинга, печатаем информацию в консоль
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
