######## LIST ########

# print(list(range(1, int(input()) + 1)))

# abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#        'w', 'x', 'y', 'z']
# n = int(input())
# print(abc[0:n])

# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers) + max(numbers))

# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
#
# print(average)

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# rainbow[-1] = 'Фиолетовый'
# print(rainbow)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers), numbers[-1], numbers[::-1], 'YES' if 5 in numbers and 17 in numbers else 'NO', numbers[1:-1],
#       sep='\n')

# lst = []
# num = int(input())
# for i in range(num):
#     lst.append(input())
# print(lst)

# lst = []
# for i in range(26):
#     lst.append(chr(ord('a') + i) * (i + 1))
# print(lst)

# lst = []
# num = int(input())
# for i in range(num):
#     lst.append(int(input()) ** 3)
# print(lst)

# lst = []
# num = int(input())
# for i in range(1, num + 1):
#     if num % i == 0:
#         lst.append(i)
# print(lst)

# lst = []
# num = int(input())
# x = int(input())
# for _ in range(num - 1):
#     y = int(input())
#     lst.append(x + y)
#     x = y
# print(lst)

# lst = []
# num = int(input())
# for _ in range(num):
#     lst.append(int(input()))
# del lst[1::2]
# print(lst)

# lst = []
# num = int(input())
# for i in range(num):
#     lst.append(input())
# num_2 = int(input())
# for i in lst:
#     if len(i) < num_2:
#         continue
#     else:
#         print(i[num_2 - 1], end='')

# lst = []
# num = int(input())
# for i in range(num):
#     lst.extend(input())
# print(lst)

# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# lst = []
# for num in numbers:
#     lst.append(num ** 2)
# print(sum(lst))

# num = int(input())
# lst = []
# for i in range(num):
#     lst.append(int(input()))
# print(*lst, sep='\n')
# print()
# for num in lst:
#     print(num ** 2 + num * 2 + 1)

# num = int(input())
# lst = [int(input()) for _ in range(num)]
# del lst[lst.index(max(lst))]
# del lst[lst.index(min(lst))]
# print(*lst, sep='\n')

# num = int(input())
# lst = []
# for _ in range(num):
#     st = input()
#     if st not in lst:
#         lst.append(st)
# print(*lst, sep='\n')

# num = int(input())
# lst = []
# for _ in range(num):
#     lst.append(input())
# req = input().lower()
# for i in lst:
#     if req in i.lower():
#         print(i)

# num = int(input())
# lst = []
# for _ in range(num):
#     lst.append(input())
# num2 = int(input())
# lst2 = []
# for _ in range(num2):
#     lst2.append(input())
# lst3 = []
# for i in lst:
#     count = 0
#     for j in lst2:
#         if j.lower() in i.lower():
#             count += 1
#     if count == len(lst2):
#         lst3.append(i)
# print(*lst3, sep='\n')

# num = int(input())
# negatives = []
# zeros = []
# positives = []
# for _ in range(num):
#     n = int(input())
#     if n > 0:
#         positives.append(n)
#     elif n == 0:
#         zeros.append(n)
#     else:
#         negatives.append(n)
# print(*negatives, *zeros, *positives, sep='\n')

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# lst = input().split()
# print(*lst, sep='\n')

# lst = input().split()
# print(f'{lst[0][0]}.{lst[1][0]}.{lst[2][0]}.')

# st = input().split('\\')
# print(*st, sep='\n')

# lst = list(map(int, input().split()))
# for c in lst:
#     print('+' * c)

# lst = list(map(int, input().split('.')))
# flag = True
# for c in lst:
#     if c > 255:
#         flag = False
#         break
# print('ДА' if flag else 'НЕТ')

# st = input()
# raz = input()
# print(raz.join(st))

# lst = list(map(int, input().split()))
# count = 0
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j]:
#             count += 1
# print(count)

# numbers = [8, 9, 10, 11]
# numbers.remove(10)
# numbers.insert(2, 17)
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
# numbers.remove(8)
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)

# lst = list(map(int, input().split()))
# maximum = lst.index(max(lst))
# minimum = lst.index(min(lst))
# lst[maximum], lst[minimum] = lst[minimum], lst[maximum]
# print(*lst)

# lst = input().lower().split()
# a = lst.count('a')
# an = lst.count('an')
# the = lst.count('the')
# print(f'Общее количество артиклей: {a + an + the}')

# num = int(input()[1:])
# lst = []
# for i in range(num):
#     st = input().split('#')
#     lst.append(st[0].rstrip())
# print(*lst, sep='\n')

# lst = list(map(int, input().split()))
# lst.sort()
# print(*lst)
# lst.sort(reverse=True)
# print(*lst)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [c[1:] for c in keywords]
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# lengths = [len(keyword) for keyword in keywords]
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
# new_keywords = [i for i in keywords if len(i) > 4]
# print(new_keywords)

# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
# print(palindromes)

# lst = [i ** 2 for i in range(1, int(input()) + 1)]
# print(*lst, sep='\n')

# print(*[int(i) ** 3 for i in input().split()])

# lst = [char for char in input().split()]
# print(*lst, sep='\n')

# lst = [i for i in input() if i.isdigit()]
# print(*lst, sep='')

# lst = list(map(int, input().split()))
# lst1 = [i ** 2 for i in lst if (i ** 2) % 10 != 4 and (i ** 2) % 2 == 0]
# print(*lst1)

# from time import time
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
#      -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
#      -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
# start = time()
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# finish = time()
# print(a)
# print(finish - start)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# n = len(a)
# for i in range(n):
#      lowest_value_index = i
#      for j in range(i + 1, n):
#           if a[j] < a[lowest_value_index]:
#                lowest_value_index = j
#      a[i], a[lowest_value_index] = a[lowest_value_index], a[i]
# print(a)

# names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
# if 'Джасмин' not in names:
#     print ('Не могу найти Джасмин.')
# else:
#     print('Ceмья Джасмин: ', end='')
#     print(names)

# n = int(input())
# lst = [i for i in range(n+1)]
# print(lst[2::2])

# lst_1 = [int(i) for i in input().split()]
# lst_2 = [int(i) for i in input().split()]
# lst = []
# for i in range(len(lst_1)):
#     lst.append(int(lst_1[i]) + int(lst_2[i]))
# print(*lst)

# lst = [int(i) for i in input().split()]
# print(*lst, sep='+', end='')
# print(f'={sum(lst)}')

# st = input().split('-')
# st2 = ''.join(st)
# if st2.isdigit():
#     if (st[0] == '7' and len(st[1]) == 3 and len(st[2]) == 3 and len(st[3]) == 4) or (
#             len(st[0]) == 3 and len(st[1]) == 3 and len(st[1]) == 3):
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# print(max([len(i) for i in input().split()]))

# lst = [i for i in input().split()]
# lst2 = []
# for i in lst:
#     word = i[1:] + i[:1] + 'ки'
#     lst2.append(word)
# print(*lst2)
