# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


n = InputNumbers('Введите число n: ')

my_list = {n: ((1 + 1 / n) ** n) for n in range(1, n + 1)}
print('Последовательность чисел: ', my_list)
