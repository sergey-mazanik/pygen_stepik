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
