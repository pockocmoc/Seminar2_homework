# Реализуйте алгоритм перемешивания списка.
import random

# listA = [2, 8, 4, 3, 1, 5]
# random.shuffle(listA)
# print(listA)


basic_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный массив:\n {basic_array}')

random_array = []
for i in range(len(basic_array)):
    random_array.append(basic_array.pop(random.randint(0, len(basic_array)-1)))
print(f'Перемешанный массив:\n {random_array}')
