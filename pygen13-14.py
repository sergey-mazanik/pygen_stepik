# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print(f'*        *')
#     print('*' * 10)
#
#
# draw_box()


# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
#
# draw_triangle()


# def draw_triangle(fill: str, base: int):
#     for i in range(base // 2 + 1):
#         for j in range(i + 1):
#             print(fill, end='')
#         print()
#     for i in range(base // 2, 0, -1):
#         for j in range(i, 0, -1):
#             print(fill, end='')
#         print()
#
#
# fill = input()
# base = int(input())
# draw_triangle(fill, base)


# def print_fio(name, surname, patronymic):
#     print(f'{surname.upper()[0]}{name.upper()[0]}{patronymic.upper()[0]}')
#
#
# name, surname, patronymic = input(), input(), input()
# print_fio(name, surname, patronymic)


# def print_digit_sum(num):
#     lst = [int(i) for i in str(num)]
#     print(sum(lst))
#
#
# n = int(input())
# print_digit_sum(n)


# def convert_to_miles(km):
#     return km * 0.6214
#
#
# num = int(input())
# print(convert_to_miles(num))


# def get_days(month):
#     m31 = [1, 3, 5, 7, 8, 10, 12]
#     m30 = [4, 6, 9, 11]
#     if month in m31:
#         result = 31
#     elif month in m30:
#         result = 30
#     else:
#         result = 28
#
#     return result
#
#
# num = int(input())
# print(get_days(num))


# def get_factors(num):
#     lst = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             lst.append(i)
#     return lst
#
#
# n = int(input())
# print(get_factors(n))


# def number_of_factors(num):
#     lst = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             lst.append(i)
#     return len(lst)
#
#
# n = int(input())
# print(number_of_factors(n))


# def find_all(target, symbol):
#     lst = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             lst.append(i)
#     return lst
#
#
# s = input()
# char = input()
# print(find_all(s, char))


# def merge(list1, list2):
#     lst = list1 + list2
#     lst.sort()
#     return lst
#
#
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]
# print(merge(numbers1, numbers2))


# def quick_merge(n):
#     lst = []
#     for i in range(n):
#         lst_input = [int(c) for c in input().split()]
#         lst += lst_input
#     lst.sort()
#     return lst
#
#
# print(*quick_merge(int(input())))


# def is_valid_triangle(side1, side2, side3):
#     if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
#         return True
#     else:
#         return False
#
#
# a, b, c = int(input()), int(input()), int(input())
# print(is_valid_triangle(a, b, c))


# def is_prime(num):
#     lst = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             lst.append(i)
#     if len(lst) == 2:
#         return True
#     else:
#         return False
#
#
# n = int(input())
# print(is_prime(n))


# объявление функции
# def get_next_prime(num):
#     count = num
#     while True:
#         count += 1
#         if is_prime(count):
#             return count
#             break
#
#
# n = int(input())
# print(get_next_prime(n))


# объявление функции
# def is_password_good(password):
#     count_up = 0
#     count_low = 0
#     count_dig = 0
#     if len(password) < 8:
#         return False
#     for c in password:
#         if c.isupper():
#             count_up += 1
#         if c.islower():
#             count_low += 1
#         if c.isdigit():
#             count_dig += 1
#     if count_up != 0 and count_low != 0 and count_dig != 0:
#         return True
#     else:
#         return False
#
#
# txt = input()
# print(is_password_good(txt))


# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) != len(word2):
#         return False
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#     # else:
#     #     return False
#
#
#
# txt1 = input()
# txt2 = input()
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
#     text1 = "".join(i for i in text if i.isalpha())
#     if text1.lower()[:] == text1.lower()[::-1]:
#         return True
#     else:
#         return False
#
#
# txt = input()
# print(is_palindrome(txt))

# def is_prime(num):
#     lst = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             lst.append(i)
#     if len(lst) == 2:
#         return True
#     else:
#         return False
#
# def is_palindrome(text):
#     text1 = "".join(i for i in text if i.isalpha())
#     if text1.lower()[:] == text1.lower()[::-1]:
#         return True
#     else:
#         return False
#
# def is_valid_password(password):
#     password = password.split(':')
#     count = 0
#     a = password[0]
#     b = int(password[1])
#     c = int(password[2])
#     if len(password) != 3:
#         return False
#     if a[:] == a[::-1]:
#         count += 1
#     if is_prime(b):
#         count += 1
#     if c % 2 == 0:
#         count += 1
#
#     if count == 3:
#         return True
#     else:
#         return False
#
# psw = input()
# print(is_valid_password(psw))


# def is_correct_bracket(text):
#     count = 0
#     for i in range(len(text)):
#         if count < 0:
#             break
#         elif text[0] == ')':
#             count = -1
#         elif text[i] == '(':
#             count += 1
#         else:
#             count -= 1
#     if count == 0:
#         return True
#     else:
#         return False
#
#
# txt = input()
# print(is_correct_bracket(txt))


# def convert_to_python_case(text):
#     st = text[0].lower()
#     for i in text[1:]:
#         if i.isupper():
#             st = st + '_' + i.lower()
#         else:
#             st += i.lower()
#     return st
#
#
# txt = input()
# print(convert_to_python_case(txt))


# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y
#
#
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# from math import pi
#
#
# def get_circle(radius):
#     length = 2 * pi * radius
#     square = pi * radius ** 2
#     return length, square
#
#
# r = float(input())
# length, square = get_circle(r)
# print(length, square)


# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     x3 = (-b) / (2 * a)
#     if d > 0:
#         return min(x1, x2), max(x1, x2)
#     elif d == 0:
#         return x3, x3
#     else:
#         return 'Нет корней'
#
#
# a, b, c = int(input()), int(input()), int(input())
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# def get_shipping_cost(quantity):
#     if quantity == 1:
#         return 1000
#     else:
#         return 1000 + 120 * (quantity - 1)
#
#
# n = int(input())
# print(get_shipping_cost(n))


# from math import factorial
# def compute_binom(n, k):
#     bin = factorial(n) / (factorial(k) * factorial(n - k))
#     return int(bin)
#
#
# n = int(input())
# k = int(input())
# print(compute_binom(n, k))


# def number_to_words(num):
#     dig = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     dec = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
#            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     teen = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
#             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     if 0 < num <= 9:
#         return dig[num]
#     if num % 10 == 0:
#         return dec[int(num / 10)]
#     if 10 < num <= 19:
#         return teen[num - 10]
#     if 19 < num < 100 and num % 10 != 0:
#         return dec[num // 10] + ' ' + dig[num % 10]
#
#
# n = int(input())
# print(number_to_words(n))


# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
#               'декабрь']
#
#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#               'november', 'december']
#     if language == 'ru':
#         return lng_ru[number-1]
#     if language == 'en':
#         return lng_en[number-1]
#
# lan = input()
# num = int(input())
# print(get_month(lan, num))


# def is_magic(date):
#     lst = date.split('.')
#     if int(lst[0]) * int(lst[1]) == int(lst[2][2:]):
#         return True
#     else:
#         return False
#
#
# date = input()
# print(is_magic(date))


# def is_pangram(text):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     for i in abc:
#         if i not in text.lower():
#             return False
#     return True
#
#
# text = input()
# print(is_pangram(text))
