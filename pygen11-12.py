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
