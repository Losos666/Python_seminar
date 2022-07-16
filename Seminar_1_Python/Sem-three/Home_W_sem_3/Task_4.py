# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = 45
 
print(f"{n:b}")
 
 
b = ''
while n > 2:
    b = str(n % 2) + b
    n = n // 2
b = str(n) + b
print(b)
