"""
3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
обработать данные, найти среднюю цену и вывести ее, а также
сделать гистограмму цен на диваны
"""

"""
Этот блок парсит цены на диваны с сайта divan.ru и пишет их в csv файл
в виде таблицы: "Название дивана", "Цена"
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Путь к драйверу Firefox
geckodriver_path = r'C:\knzv\geckodriver-v0.35.0-win64\geckodriver.exe'

# Настройка опций Firefox
firefox_options = Options()
# firefox_options.add_argument('--headless')  # Запуск в фоновом режиме (без интерфейса)

# Инициализация драйвера Firefox
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

# URL страницы с диванами и креслами
url = 'https://www.divan.ru/chelyabinsk/category/divany-i-kresla'
driver.get(url)

# Подождите, пока страница полностью загрузится
time.sleep(10)
print(driver.execute_script("return document.body.scrollHeight"))

# Функция для прокрутки страницы вниз
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Установите начальную высоту страницы
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Прокрутите страницу до самого низа
    scroll_to_bottom()

    # Подождите, пока новый контент загрузится
    time.sleep(10)

    # Получите текущую высоту страницы
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Условие выхода из цикла: если высота страницы не изменяется, значит, мы достигли конца страницы
    if new_height == last_height:
        break

    last_height = new_height
    print(last_height)

# Создание списка для хранения данных о диванах
sofas = []

# Поиск всех товаров на странице
products = driver.find_elements(By.CLASS_NAME, 'wYUX2')
for product in products:
    try:
        # Получение названия товара
        title_element = product.find_element(By.TAG_NAME,'a')
        title = title_element.text

        if 'диван' in title.lower():
            try:
                # Получение цены товара
                price_element = product.find_element(By.CLASS_NAME, 'ui-LD-ZU')
                price_draft = price_element.text
                price = price_draft.replace(' ','')[0: -4]

                # Добавление данных о диване в список
                sofas.append({'Title': title, 'Price': price})
            except Exception as e:
                print(f"Ошибка при получении цены для {title}: {e}")
                continue

    except Exception as e:
        print(f"Ошибка при обработке товара: {e}")
        continue


# Закрытие драйвера
driver.quit()

# Создание DataFrame и сохранение данных в CSV файл
df = pd.DataFrame(sofas)
df.to_csv('sofas_prices.csv', index=False)

print("Данные сохранены в файл sofas_prices.csv")
