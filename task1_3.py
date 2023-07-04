"""
    --Task1_3--
Задание №8
Нарисовать в консоли ёлку спросив у пользователя количество рядов.
"""


def draw_tree(levels):
    for i in range(1, levels + 1):
        print(" " * (levels - i), end="")
        print("*" * (2 * i - 1))


while True:
    rows = int(input("Введите количество рядов ёлки: "))

    if rows > 0:
        break
    else:
        print("Ошибка: Количество рядов должно быть положительным числом.")

draw_tree(rows)
