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

# n = int(input())
# max_num1 = 0
# max_num2 = 0
# for _ in range(n):
#     a = int(input())
#     if a > max_num1:
#         max_num2 = max_num1
#         max_num1 = a
#     elif max_num2 < a < max_num1:
#         max_num2 = a
# print(max_num1, max_num2, sep='\n')

# flag = True
# for _ in range(10):
#     num = int(input())
#     if num % 2 != 0:
#         flag = False
#         break
# print('YES' if flag else 'NO')

# n = int(input())
# a = 1
# y = 0
# for i in range(1, n + 1):
#     b = a
#     a = b + y
#     y = b
#     print(b, end=' ')

# text = input()
# while text != 'КОНЕЦ':
#     print(text)
#     text = input()

# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()

# text = input()
# count = 0
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     count += 1
#     text = input()
# print(count)

# num = int(input())
# while num % 7 == 0:
#     print(num)
#     num = int(input())


# num = int(input())
# summa = 0
# while num >= 0:
#     summa += num
#     num = int(input())
# print(summa)

# num = int(input())
# count = 0
# while 0 < num < 6:
#     if num == 5:
#         count += 1
#     num = int(input())
# print(count)

# num = int(input())
# count = 0
# while num >= 25:
#     count += 1
#     num -= 25
# while num >= 10:
#     count += 1
#     num -= 10
# while num >= 5:
#     count += 1
#     num -= 5
# while num >= 1:
#     count += 1
#     num -= 1
# print(count)

# num = int(input())
# has_seven = False  # сигнальная метка
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven:
#     print('YES')
# else:
#     print('NO')

# num = int(input())
# while num != 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10

# num = int(input())
# while num != 0:
#     last_digit = num % 10
#     print(last_digit, end='')
#     num = num // 10

# num = int(input())
# last_digit = num % 10
# maximum = last_digit
# minimum = last_digit
# while num != 0:
#     last_digit = num % 10
#     if last_digit > maximum:
#         maximum = last_digit
#     elif last_digit <= minimum:
#         minimum = last_digit
#     num = num // 10
# print(f'''Максимальная цифра равна {maximum}
# Минимальная цифра равна {minimum}''')

# num = int(input())
# summa = 0
# count = 0
# multi = 1
# first_digit = int(str(num)[0])
# sum_first_last = num % 10 + first_digit
# while num != 0:
#     last_digit2 = num % 10
#     count += 1
#     summa += last_digit2
#     multi *= last_digit2
#     num = num // 10
# sred = summa / count
# print(summa, count, multi, sred, first_digit, sum_first_last, sep='\n')

# print(input()[1])

# num = int(input())
# last_digit = num % 10
# flag = True
# while num != 0:
#     last_digit2 = num % 10
#     if last_digit2 != last_digit:
#         print('NO')
#         flag = False
#         break
#     else:
#         num = num // 10
# if flag:
#     print('YES')

# num = int(input())
# flag = True
# last_digit = num % 10
# while num != 0:
#     last_digit2 = num % 10
#     if last_digit2 < last_digit:
#         flag = False
#         break
#     else:
#         last_digit = last_digit2
#         num = num // 10
# print('YES' if flag else 'NO')

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i -= 20

# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')

# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# num = int(input())
# for i in range(2, num + 1):
#     if num % i == 0:
#         print(i)
#         break

# num = int(input())
# for i in range(1, num + 1):
#     if 5 <= i <= 9:
#         continue
#     elif 17 <= i <= 37:
#         continue
#     elif 78 <= i <= 87:
#         continue
#     print(i)

# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')

# count = 0
# p = 1
# for _ in range(10):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# mx = -10 ** 6
# summa = 0
# for _ in range(10):
#     x = int(input())
#     if x < 0:
#         summa += x
#         if x > mx:
#             mx = x
# if summa != 0:
#     print(summa)
#     print(mx)
# else:
#     print('NO')

# s = 0
# for _ in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)

# n = int(input())
# max_digit = -1
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0 and digit > max_digit:
#         max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# while n >= 10:
#     n //= 10
# print(n)

# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# n = int(input())
# for i in range(1, n+1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(f'{i} + {j} = {i + j}')
#     print()

# n = int(input())
# for i in range(n // 2 + 1):
#     for j in range(i + 1):
#         print('*', end='')
#     print()
# for i in range(n // 2, 0, -1):
#     for j in range(i, 0, -1):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end='')
#     print()

# for n in range(1, 19):
#     for k in range(1, 19):
#         for m in range(1, 19):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(f'n = {n}, k = {k}, m = {m}')

# for n in range(1, 100):
#     for k in range(1, 100):
#         for m in range(1, 100):
#             if n * 10 + k * 5 + m * 0.5 == 100 and n + k + m == 100:
#                 print(f'n = {n}, k = {k}, m = {m}')

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     while e ** 5 <= a ** 5 + b ** 5 + c ** 5 + d ** 5:
#                         if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                             print(a + b + c + d + e)

# n = int(input())
# total = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(total, end=' ')
#         total += 1
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()

# a, b = int(input()), int(input())
# summa = 0
# maximum = 0
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += j
#         if count >= summa:
#             summa = count
#             maximum = i
# print(maximum, summa)

# n = int(input())
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     print(f'{i}{"+" * count}', sep='')

# n = int(input())
# while n > 9:
#     count = 0
#     while n > 0:
#         last_digit = n % 10
#         count += last_digit
#         n //= 10
#     n = count
# print(n)

# from math import factorial
#
# n = int(input())
# summa = 0
# for i in range(1, n + 1):
#     summa += factorial(i)
# print(summa)

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, b + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)

# n = int(input())
# s = 0
# while n != 0:
#     last_digit = n % 10
#     if last_digit % 2 == 0:
#         s += last_digit
#     n //= 10
# print(s)

# n = 8
# count = 0
# maximum = -10 ** 6
# for _ in range(n):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4
# count = 0
# maximum = -10 ** 8
# for _ in range(n):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# print('*' * 19)
# for i in range(n - 2):
#     print(f'*{" " * 17}*')
# print('*' * 19)

# print(input()[2])

# n = int(input())
# summa_5 = 0
# count_3 = 0
# last_digit = n % 10
# count_last = 0
# multi_7 = 1
# count_0_5 = 0
# odd = 0
# while n != 0:
#     a = n % 10
#     if a == 3:
#         count_3 += 1
#     if a == last_digit:
#         count_last += 1
#     if a % 2 == 0:
#         odd += 1
#     if a > 5:
#         summa_5 += a
#     if a > 7:
#         multi_7 *= a
#     if a == 0 or a == 5:
#         count_0_5 += 1
#     n //= 10
# print(count_3, count_last, odd, summa_5, multi_7, count_0_5, sep='\n')

# lst = []
# for n in range(1, 33):
#     for k in range(1, 33):
#         for m in range(1, 33):
#             for i in range(1, 33):
#                 if n ** 3 + k ** 3 == m ** 3 + i ** 3 and n != k and n != m and n != i and k != m and k != i and m != i:
#                     lst.append(n ** 3 + k ** 3)
#                     # print(n ** 3 + k ** 3)
# my_set = set(lst)
# print(sorted(my_set))
