"""
    --Task4
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Угадайте число от 0 до 1000. У вас 10 попыток.")

for attempt in range(1, MAX_ATTEMPTS + 1):
    guess = int(input(f"Попытка {attempt}: Введите вашу догадку: "))

    if guess == num:
        print("Поздравляю! Вы угадали число!")
        break
    elif guess < num:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")

    if attempt == MAX_ATTEMPTS:
        print("У вас закончились попытки. Загаданное число:", num)
