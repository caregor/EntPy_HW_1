"""
    --Task 3--
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на
единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
def is_prime_number(n):

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    num = int(input("Введите число: "))

    if num >= 0 and num <= 100000:
        break
    else:
        print("Ошибка: Число должно быть неотрицательным и не больше 100000.")

if is_prime_number(num):
    print(f"Число {num} является простым.")
else:
    print(f"Число {num} является составным.")
