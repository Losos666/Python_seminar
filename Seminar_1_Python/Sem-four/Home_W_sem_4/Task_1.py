# Вычислить число c заданной точностью d 
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# работаем с числом PI (корректировка на лекции)


# (использую метод из семинара- 3 задание -3 ) - он не округляет сумму после точки.
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
def toFixed( max : float , n = 0):
    a , b = str(max).split('.')
    return' {}.{} {}'.format(a,b[:n], '0'*(n-len(b)))


import math
number_pi = math.pi
print(toFixed(number_pi,3))

# не совсем понял такое решение нужно или нет. 