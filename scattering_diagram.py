"""
2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных
 с помощью функции `numpy.random.rand`.

import numpy as np
random_array = np.random.rand(5)  # массив из 5 случайных чисел
print(random_array)
"""

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
np.random.seed(0)
# x1 = np.random.rand(100)
# Задаем диапазон Х для первого набора данных от 0 до 60
x1 = np.linspace(0, 60, 100)
y1 = np.random.rand(100)    # Задаём не 5, а 100 случайных чисел

# x2 = np.random.rand(100)
# Задаем диапазон Х для второго набора данных от 40 до 100
x2 = np.linspace(40, 100, 100)
y2 = np.random.rand(100)    # Задаём не 5, а 100 случайных чисел

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 6))

# Первый набор данных (красные кружки)
plt.scatter(x1, y1, color='red', marker='o', label='Набор 1')

# Второй набор данных (синие крестики)
plt.scatter(x2, y2, color='blue', marker='x', label='Набор 2')

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# Добавление легенды
plt.legend()

# Показ графика
plt.show()
