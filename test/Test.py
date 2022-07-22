# from ast import If


print('введите выбор - 1 или 2')
number1 = int(input('введите число N --> '))
startstop = 1
if startstop == number1:
    print('выбор 1 ')
else:
    print('выбор 2 ')

# def quest_vopr():
#     print('введите выбор - 1 или 2')
# number1 = int(input('введите число N --> '))
# startstop = 1
# if startstop == number1:
#     print('выбор 1 ')
# else:
#     print('выбор 2 ')


# определение четного и нечетного числа

# def number_once_def(number1):
#     if number1 % 2 == 0:
#      print('четное')
#     else:
#         print('не четно')
# number_once_def(6

user =['user1', 'user2','user3','user4', 'user5','user6']
ids  =[1,2,3,4,5,6,]
data = list(zip(user ,ids))
print(data)