import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import email, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # max размер экрана
    driver.maximize_window()
    driver.get('https://petfriends.skillfactory.ru/login')
    # Вводим email
    driver.find_element(By.ID, 'email').send_keys(email)
    # time.sleep(3)  # небольшая задержка
    # Вводим пароль
    driver.find_element(By.ID, 'pass').send_keys(password)
    # time.sleep(3)  # небольшая задержка
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    yield driver

    driver.quit()

def test_show_my_pets(driver):
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # time.sleep(3)  # небольшая задержка
    driver.get('https://petfriends.skillfactory.ru/my_pets')
    # time.sleep(3)  # небольшая задержка
    wait = WebDriverWait(driver, 3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="all_my_pets"]')))
    statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    # time.sleep(3)  # небольшая задержка
    pets_cards = driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")
    # time.sleep(3)  # небольшая задержка
    # Количество питомцев взято из статистики пользователя
    count = statistic[0].text.split('\n')
    count = count[1].split(' ')
    count = int(count[1])
    # Количество карточек
    count_of_pets = len(pets_cards)
    # Сравниваем кол-во полученных карточек
    assert count == count_of_pets

def test_show_my_pets_photo(driver):
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # time.sleep(3)  # небольшая задержка
    driver.get('https://petfriends.skillfactory.ru/my_pets')
    # time.sleep(3)  # небольшая задержка
    wait = WebDriverWait(driver, 3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]/h2')))
    statistic = driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    # time.sleep(3)  # небольшая задержка
    img = driver.find_elements(By.CSS_SELECTOR, ".table.table-hover img")
    # time.sleep(3)  # небольшая задержка
    # Количество питомцев взято из статистики пользователя
    count = statistic[0].text.split('\n')
    count = count[1].split(' ')
    count = int(count[1])
    # Хотя бы у половины питомцев есть фото
    cards = count // 2
    count_photo = 0
    for i in range (len(img)):
        if img[i].get_attribute('src') != '':
            count_photo += 1
    assert count_photo == cards

def test_show_my_pets_name_age(driver):
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.get('https://petfriends.skillfactory.ru/my_pets')
    driver.implicitly_wait(3)
    descriptions = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
    for i in range(len(descriptions)):
        parts = descriptions[i].text.split(' ')
        if len(parts) >= 3:
            assert len(parts[0]) > 0
            assert len(parts[1]) > 0
            assert len(parts[2]) > 0

def test_show_my_pets_name(driver):
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # time.sleep(3)  # небольшая задержка
    driver.get('https://petfriends.skillfactory.ru/my_pets')
    driver.implicitly_wait(3)
    name = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
    name_pets = []
    for data1 in range(len(name)):
        pets_data = name[data1].text.split(' ')
        name_pets.append(pets_data[0])
    for data1 in range(len(name_pets) - 1):
        for data2 in range(data1 + 1, len(name_pets)):
            # У всех питомцев разные имена
            assert name_pets[data1] != name_pets[data2]


def test_show_my_pets_no_duplicates(driver):
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    # time.sleep(3)  # небольшая задержка
    driver.get('https://petfriends.skillfactory.ru/my_pets')
    driver.implicitly_wait(3)
    all_my_pets = driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets table tbody tr')
    pets = []
    for data1 in range(len(all_my_pets)):
        pets.append(all_my_pets[data1].text.split(' '))
    for data1 in range(len(pets) - 1):
        for data2 in range(data1 + 1, len(pets)):
            # В списке нет повторяющихся питомцев. Повторяющиеся питомцы — это питомцы, у которых одинаковое имя, порода и возраст.
            assert pets[data1][0] != pets[data2][0]
            assert pets[data1][1] != pets[data2][1]
            assert pets[data1][2] != pets[data2][2]