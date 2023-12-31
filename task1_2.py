"""
    --Task 1_2--
Задание №7
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""


def process_number(number):
    if 1 <= number <= 9:
        square = number ** 2
        return f"Введено однозначное число. Квадрат числа: {square}"
    elif 10 <= number <= 99:
        digit1 = number // 10
        digit2 = number % 10
        product = digit1 * digit2
        return f"Введено двузначное число. Произведение цифр: {product}"
    elif 100 <= number <= 999:
        reversed_number = int(str(number)[::-1])
        return f"Введено трехзначное число. Зеркальное отображение: {reversed_number}"
    else:
        return "Ошибка: Введено число, не попадающее в диапазон от 1 до 999."


input_number = int(input("Введите число от 1 до 999: "))
result = process_number(input_number)
print(result)
