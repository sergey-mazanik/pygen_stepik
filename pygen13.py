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


