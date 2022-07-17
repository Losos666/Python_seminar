# Задайте последовательность чисел.
#  Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 2, 3, 3, 4, 5,99,103,5,99,1,2,3,90,666] 
 
def get_unique_numbers(numbers): 
    list_of_unique_numbers = [] 
    unique_numbers = set(numbers) 
 
    for number in unique_numbers: 
        list_of_unique_numbers.append(number) 
 
    return list_of_unique_numbers 
 
print(get_unique_numbers(numbers))