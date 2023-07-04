"""
    --Task 1_1--
Задание №6
Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print
"""

year = int(input("Введите год: "))

if year <= 0:
    print("Ошибка: Год должен быть положительным числом.")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год является високосным.")
elif year < 1582 and year % 4 == 0:
    print("Год является високосным по юлианскому календарю.")
else:
    print("Год не является високосным.")

