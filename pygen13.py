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


def is_prime(num):
    pass


n = int(input())
print(is_prime(n))