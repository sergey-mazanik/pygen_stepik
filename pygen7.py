####### LOOPS #######

# for i in range(10):
#     print('Python is awesome!')

# phrase = input()
# num = int(input())
# for i in range(num):
#     print(phrase)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# num = int(input())
# for i in range(num):
#     print('*' * 19)

# name = input()
# for i in range(10):
#     print(i, name)

# from math import pow
# num = int(input())
# for i in range(num + 1):
#     print(f'Квадрат числа {i} равен {int(pow(i, 2))}')

# num = int(input())
# for i in range(num):
#     print('*' * (num - i))

# m = int(input())
# p = int(input())
# n = int(input())
# koef = (1 + p / 100)
# for i in range(n):
#     print(i + 1, m * (koef ** i))

# m = int(input())
# n = int(input())
# for i in range(m, n+1):
#     print(i)

# m = int(input())
# n = int(input())
# if n > m:
#     for i in range(m, n+1):
#         print(i)
# elif n < m:
#     for i in range(m, n-1, -1):
#         print(i)
# else:
#     print(m)

# m = int(input())
# n = int(input())
# for i in range((m + m % 2 - 1), n-1, -2):
#     print(i)

# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

# num = int(input())
# for i in range(1, 11):
#     print(f'{num} x {i} = {num * i}')

# from math import pow
#
# num1 = int(input())
# num2 = int(input())
# count = 0
# for i in range(num1, num2 + 1):
#     if pow(i, 3) % 10 == 4 or pow(i, 3) % 10 == 9:
#         count += 1
# print(count)

# num = int(input())
# summa = 0
# for _ in range(1, num + 1):
#     a = int(input())
#     summa += a
# print(summa)

# from math import log, e
#
# n = int(input())
# q = 0
# for i in range(1, n + 1):
#     a = 1 / i
#     q += a
# print(q - log(n, e))

# from math import pow
#
# num = int(input())
# count = 0
# for i in range(1, num + 1):
#     if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
#         count += i
# print(count)

# from math import factorial
#
# print(factorial(int(input())))

# summa = 1
# for _ in range(10):
#     num = int(input())
#     if num != 0:
#         summa *= num
# print(summa)

# num = int(input())
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += i
# print(count)

# num = int(input())
# count = 0
# for i in range(num):
#     if i % 2 == 0:
#         count += i + 1
#     elif i % 2 != 0:
#         count -= i + 1
# print(count)


