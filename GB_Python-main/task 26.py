# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

def recfun(num, exponentiation):
    if exponentiation == 0:
        return 1
    return num * recfun(num, exponentiation - 1)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

print(f"A = {A}; B = {B}; -> {recfun(A, B)}") 