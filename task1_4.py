"""
    --Task1_4--
Задание №9
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
"""

for i in range(2, 10, 4):
    for j in range(2, 11):
        for k in range(i, i+4):
            result = k * j
            if j != 10:
                print(f"{k} x {j} = {result:2}", end="   ")
            else:
                print(f"{k} x {j}= {result:2}", end="   ")
        print()
    print()
