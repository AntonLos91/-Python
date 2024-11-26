# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
# 5
#    1 2 3 4 5
#    3
#    -> 1

N = int(input("Введите натуральное число N: "))
array = []
for i in range(N):
    array.append(int(input(f"Введите число N{i+1}: ")))
print(' '.join(map(str, array)))

X = int(input("Введите число X, которое необходимо найти в массиве: "))
count = 0
for i in range(N):
    if array[i] == X:
        count += 1
        
print(f"В массиве число {X} встречается {count} раз") 