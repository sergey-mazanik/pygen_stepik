######### String ##########

# s = 'All you need is love'
# if 'love' in s:
#     print('❤️')
# else:
#     print('💔')

# st = input()
# for i in range(len(st)):
#     if i % 2 == 0:
#         print(st[i])

# st = input()
# for i in range(len(st) - 1, -1, -1):
#     print(st[i])

# name = input()
# surname = input()
# name2 = input()
# print(surname[0], name[0], name2[0], sep='')

# st = input()
# summa = 0
# for i in range(len(st)):
#     summa += int(st[i])
# print(summa)

# st = input()
# flag = False
# for i in range(len(st)):
#     if st[i] in '0123456789':
#         flag = True
#         break
# print('Цифра' if flag else 'Цифр нет')

# count_plus = 0
# count_star = 0
# for c in input():
#     if c in '+':
#         count_plus += 1
#     if c in '*':
#         count_star += 1
# print(f'''Символ + встречается {count_plus} раз
# Символ * встречается {count_star} раз''')

# st = input()
# count = 0
# for i in range(len(st) - 1):
#     if st[i] == st[i + 1]:
#         count += 1
# print(count)

# count_vowels = 0
# count_consonants = 0
# for c in input().lower():
#     if c in 'ауоыиэяюёе':
#         count_vowels += 1
#     if c in 'бвгджзйклмнпрстфхцчшщ':
#         count_consonants += 1
# print(f'''Количество гласных букв равно {count_vowels}
# Количество согласных букв равно {count_consonants}''')

# print(str(bin(int(input())))[2:])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# # print(s[:12])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])

# st = input()
# print('YES' if st[:] == st[::-1] else 'NO')

# st = input()
# print(len(st), st * 3, st[0], st[:3], st[-3:], st[::-1], st[1:-1], sep='\n')

# st = input()
# print(st[2], st[-2], st[:5], st[:-2], st[::2], st[1::2], st[::-1], st[::-2], sep='\n')

# st = input()
# a = len(st) // 2 + len(st) % 2
# print(st[a:] + st[:a])

# st = input()
# print('YES' if st == st.title() else 'NO')

# print(input().swapcase())

# st = input().lower()
# check = 'хорош'
# print('YES' if check in st else 'NO')

# st = input()
# low_st = st.lower()
# count = 0
# for i in range(len(st)):
#     if st[i] not in '0123456789' and st[i] == low_st[i]:
#         count += 1
# print(count)

# s = 'abcdababa'
# print(s.replace('ab', '123'))

# st = input()
# if st.count(' ') == 0:
#     print(1)
# else:
#     print(st.count(' ') + 1)

# st = input().lower()
# a = st.count('а')
# g = st.count('г')
# c = st.count('ц')
# t = st.count('т')
# print(f'''Аденин: {a}
# Гуанин: {g}
# Цитозин: {c}
# Тимин: {t}''')

# n = int(input())
# count = 0
# for i in range(n):
#     st = input()
#     if st.count('11') >= 3:
#         count += 1
# print(count)

# st = input()
# count = 0
# for c in st:
#     if c.isdigit():
#         count += 1
# print(count)

# st = input()
# print('YES' if st.endswith('.com') or st.endswith('.ru') else 'NO')

# st = input()
# maxi = 0
# b = 0
# for c in st:
#     if st.count(c) >= maxi:
#         maxi = st.count(c)
#         b = c
# print(b)

# st = input()
# if st.count('f') == 0:
#     print('NO')
# elif st.count('f') == 1:
#     print(st.find('f'))
# else:
#     print(st.find('f'), st.rfind('f'))

# st = input()
# first = st.find('h')
# last = st.rfind('h')
# print(st[:first] + st[last+1:])

# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# year = 2010
# amount = '10k'
# currency = 'Bitcoin'
# print(s.format(year, amount, currency))

# year = 2010
# amount = '10K'
# currency = 'Bitcoin'
#
# print(f'In {year}, someone paid {amount} {currency} for two pizzas.')


