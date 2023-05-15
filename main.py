
from methods import *

# Читаем датасет
df = pd.read_csv('dataset.csv')

# Предварительная обработка
analyze(df)

# Визуализация
visualization(df)

# Создание новых признаков
# Признак, который я бы добавил в датасет, это КПД поезда, ведь всегда хочется, чтобы расход дорогого топлива
# был меньше. Этот признак хорошо характеризует качество поезда. По имеющимся данным КПД получить не просто,
# ведь расход топлива зависит не только от массы, но и от пройденного расстояния, числа остановок и типа поезда.

# Гипотезы
hypothesis(df)

# Машинное обучение
machine_learning(df)
