# a, b = input(), input()
# print('Пароль принят' if a == b else 'Пароль не принят')

# print('Четное' if int(input()) % 2 == 0 else 'Нечетное')

# num = int(input())
# fourth = num % 10
# third = (num // 10) % 10
# second = (num // 100) % 10
# first = num // 1000
# print('ДА' if (first + fourth) == (second - third) else 'НЕТ')

# print('Доступ запрещен' if int(input()) < 18 else 'Доступ разрешен')

# a = int(input())
# b = int(input())
# c = int(input())
# print('YES' if (a < b < c and c - b == b - a) or (a > b > c and a - b == b - c) else 'NO')

# a = int(input())
# b = int(input())
# print(b if a > b else a)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# lst = [a, b, c, d]
# print(min(lst))

# age = int(input())
# if 0 < age <= 13:
#     print('детство')
# elif 14 <= age < 25:
#     print('молодость')
# elif 25 <= age < 60:
#     print('зрелость')
# elif age >= 60:
#     print('старость')

# a = int(input())
# b = int(input())
# c = int(input())
# lst = []
# if a > 0:
#     lst.append(a)
# if b > 0:
#     lst.append(b)
# if c > 0:
#     lst.append(c)
# print(sum(lst))

# num = int(input())
# print('Принадлежит' if -1 < num < 17 else 'Не принадлежит')

# # num = int(input())
# print('Не принадлежит' if -3 < int(input()) < 7 else 'Принадлежит')

# num = int(input())
# print('Принадлежит' if -30 < num <= -2 or 7 < num <= 25 else 'Не принадлежит')

# num = input()
# print('YES' if len(num) == 4 and (int(num) % 7 == 0 or int(num) % 17 == 0) else 'NO')

# a = int(input())
# b = int(input())
# c = int(input())
# print('YES' if (a + b > c) and (a + c > b) and (b + c > a) else 'NO')

# year = int(input())
# print('YES' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'NO')

# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
# print('YES' if a1 == b1 or a2 == b2 else 'NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print('YES' if (-1 <= a - c <= 1) and (-1 <= b - d <= 1) else 'NO')

# n, k = int(input()), int(input())
# if n > k:
#     print('NO')
# elif n < k:
#     print('YES')
# else:
#     print("Don't know")

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Равносторонний')
# elif a == b != c or a != b == c or a == c != b:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# a = int(input())
# b = int(input())
# c = int(input())
# if a < b < c or a > b > c:
#     print(b)
# elif a < c < b or a > c > b:
#     print(c)
# else:
#     print(a)

# month = int(input())
# m31 = [1, 3, 5, 7, 8, 10, 12]
# m30 = [4, 6, 9, 11]
# if month in m31:
#     print(31)
# elif month in m30:
#     print(30)
# else:
#     print(28)

# num = int(input())
# if num < 60:
#     print('Легкий вес')
# elif 60 <= num < 64:
#     print('Первый полусредний вес')
# else:
#     print('Полусредний вес')

# num1 = int(input())
# num2 = int(input())
# oper = input()
# if oper == '+':
#     print(num1 + num2)
# elif oper == '-':
#     print(num1 - num2)
# elif oper == '*':
#     print(num1 * num2)
# elif oper == '/':
#     if num2 == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(num1 / num2)
# else:
#     print('Неверная операция')

# color1 = input()
# color2 = input()
# colors = ['красный', 'синий', 'желтый']
# if color1 not in colors or color2 not in colors:
#     print('ошибка цвета')
# elif color1 == color2:
#     print(color1)
# elif (color1 == 'красный' and color2 == 'синий') or (color1 == 'синий' and color2 == 'красный'):
#     print('фиолетовый')
# elif (color1 == 'красный' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'красный'):
#     print('оранжевый')
# elif (color1 == 'синий' and color2 == 'желтый') or (color1 == 'желтый' and color2 == 'синий'):
#     print('зеленый')

# num = int(input())
# if num < 0 or num > 36:
#     print('ошибка ввода')
# elif num == 0:
#     print('зеленый')
# elif num % 2 == 0 and (0 < num <= 10 or 19 <= num <= 28):
#     print('черный')
# elif num % 2 == 0 and (11 <= num <= 18 or 29 <= num <= 36):
#     print('красный')
# elif num % 2 != 0 and (0 < num <= 10 or 19 <= num <= 28):
#     print('красный')
# elif num % 2 != 0 and (11 <= num <= 18 or 29 <= num <= 36):
#     print('черный')
