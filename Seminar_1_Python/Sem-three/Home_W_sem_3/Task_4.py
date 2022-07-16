# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from ast import Str


number = int(input('введите число -->  '))
print(f"{number:b}")
Stri = ''
while number > 2:
    Stri = Str(number % 2) + Stri
    number = number // 2
Stri = Stri(number) + Stri
print(number)
