# number = int(input())
# count = 1
# while number > 2:
#     number /= 2
#     count += 1
# print(count)


# -------------- Числовая угодайка -----------------
import random

# def is_valid(n):  # проверка на соответствие введенного значения условию
#     return n.isdigit() and float(n) - int(float(n)) == 0 and 1 <= int(n) <= 100
#

# def input_num():  # ввод данных
#     while True:
#         guess = input()
#         if is_valid(guess):
#             return int(guess)
#         else:
#             print('А может быть все-таки введем целое число от 1 до 100?')
#
#
# def compare_num(down_num, up_num):  # Сравнение введенного значения с загаданным
#     num = random.randint(down_num, up_num)
#     total = 0
#     while True:
#         n = input_num()
#         total += 1
#         if n < num:
#             print('Не угадали, попробуйте число побольше')
#         elif n > num:
#             print('Мимо, назовите число поменьше')
#         else:
#             print('Победа!!! Вы угадали ответ за', total, 'попыток, поздравляем!')
#             break
#
#
# def continue_game():  # Предложение продолжить игру
#     ans = input('Хотите продолжить ("д"/"н")?\n')
#     while True:
#         if ans not in ('y', 'д', 'n', 'н'):
#             ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
#         elif ans in ('n', 'н'):
#             print('До новых встреч!!!')
#             return False
#         else:
#             return True
#
#
# def game():  # Запуск игры
#     print('Добро пожаловать в числовую угадайку!')
#     while True:
#         print('Укажите, в каком диапазоне Вы готовы угадывать числа\n(В пределах от 1 до 100):\n')
#         x, y = input_num(), input_num()
#         if x > y:
#             x, y = y, x
#         print('Введите число от', x, 'до', y, '\n')
#         compare_num(x, y)
#         if continue_game():
#             continue
#         else:
#             break
#
#
# game()  # Вызов игры


# -------------- Магический шар 8 ----------------
# from random import choice
# import emoji
#
# if __name__ == '__main__':
#     list_answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Опеределенно да', 'Можешь быть уверен да',
#                     'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят да', 'Да',
#                     'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
#                     'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет',
#                     'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
#     request = ['Задавай вопрос', 'Пиши вопрос и я дам на него ответ', 'Отлично. Теперь можешь задавать свой вопрос',
#                'Задавай свой вопрос']
#     print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
#     print('А вас как зовут?')
#     user_name = input()
#     print(f'Привет {user_name}')
#     while True:
#         ball_answer = choice(list_answers)
#         ball_request = choice(request)
#         print(ball_request, user_name)
#         user_ans = input()
#         print(ball_answer, user_name)
#         print('Ко мне вопросы остались?')
#         user_last_quest = input()
#         if user_last_quest.lower() == 'нет' or user_last_quest.lower() == 'no':
#             print(emoji.emojize('Пока. Обращайся, если что :thumbs_up:'))
#             break


# ------------ Генератор безопасных паролей ---------------
# from random import choice
#
#
# # функции на запрос данных у пользователя
# def count():
#     n = input('Сколько нужно паролей? Укажи цифру: ')
#     while n.isdigit() == False:
#         print('Нужно вводить цифу, дубина!')
#         n = input('Сколько нужно паролей? Укажи цифру: ')
#     return int(n)
#
#
# def long():
#     l = input('Введи длину пароля: ')
#     while l.isdigit() == False:
#         print('Нужно вводить цифу, дубина!')
#         l = input('Введи длину пароля: ')
#     return int(l)
#
#
# def is_number():
#     isn = input('Нужны ли в пароле цифры 0123456789? Напиши "да" или "нет": ')
#     while isn.lower() not in ['да', 'нет']:
#         print('Нужно вводить "да" или "нет".')
#         isn = input('Нужны ли в пароле цифры 0123456789? Напиши "да" или "нет": ')
#     return isn
#
#
# def is_upper():
#     isup = input('Нужны ли в пароле заглавные буквы? Напиши "да" или "нет": ')
#     while isup.lower() not in ['да', 'нет']:
#         print('Нужно вводить "да" или "нет".')
#         isup = input('Нужны ли в пароле заглавные буквы? Напиши "да" или "нет": ')
#     return isup
#
#
# def is_lower():
#     islw = input('Нужны ли в пароле строчные буквы? Напиши "да" или "нет": ')
#     while islw.lower() not in ['да', 'нет']:
#         print('Нужно вводить "да" или "нет".')
#         islw = input('Нужны ли в пароле строчные буквы? Напиши "да" или "нет": ')
#     return islw
#
#
# def is_symbol():
#     issmb = input('Нужны ли в пароле символы? Напиши "да" или "нет": ')
#     while issmb.lower() not in ['да', 'нет']:
#         print('Нужно вводить "да" или "нет".')
#         issmb = input('Нужны ли в пароле символы? Напиши "да" или "нет": ')
#     return issmb
#
#
# def is_ambiguous():
#     amb = input('Будут ли в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
#     while amb.lower() not in ['да', 'нет']:
#         print('Нужно вводить "да" или "нет".')
#         amb = input('Могут ли быть в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
#     return amb
#
#
# # собираем возможные для пользователя символы в кучу
# def gen_chars():
#     chars = ''
#     if isn == 'да':
#         chars += '0123456789'
#     if isup == 'да':
#         chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     if islw == 'да':
#         chars += 'abcdefghijklmnopqrstuvwxyz'
#     if issmb == 'да':
#         chars += '!#$%&*+-=?@^_'
#     if amb == 'нет':
#         for i in range(len(chars)):
#             if chars[i] in 'il1Lo0O':
#                 del chars[i]
#     return chars
#
#
# # делаем пароли
# def build_password():
#     for i in range(n):
#         password = []
#         for i in range(l):
#             password.append(choice(chars))
#         print(''.join(password))
#
#
# # старт программы
# n = count()
# l = long()
# isn = is_number()
# isup = is_upper()
# islw = is_lower()
# issmb = is_symbol()
# amb = is_ambiguous()
# chars = gen_chars()
# build_password()


# ----------- Шифр цезаря -------------
# encryption_or_decryption = input('Шифрование или дешифрование? ')
# language = input('Русский или английский? ')
# k = int(input('Шаг сдвига (со сдвигом вправо)? '))
# alphabet_RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# alphabet_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
# alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
# s = input('Введите строку: ')
# s1 = ''
# if encryption_or_decryption.lower() == 'шифрование':
#     if language.lower() == 'русский':
#         for c in s:
#             if c in alphabet_RU:
#                 s1 += alphabet_RU[(alphabet_RU.find(c) + k) % 32]
#             elif c in alphabet_ru:
#                 s1 += alphabet_ru[(alphabet_ru.find(c) + k) % 32]
#             else:
#                 s1 += c
#     elif language.lower() == 'английский':
#         for c in s:
#             if c in alphabet_EN:
#                 s1 += alphabet_EN[(alphabet_EN.find(c) + k) % 26]
#             elif c in alphabet_en:
#                 s1 += alphabet_en[(alphabet_en.find(c) + k) % 26]
#             else:
#                 s1 += c
# if encryption_or_decryption.lower() == 'дешифрование':
#     if language.lower() == 'русский':
#         for c in s:
#             if c in alphabet_RU:
#                 s1 += alphabet_RU[(alphabet_RU.find(c) - k) % 32]
#             elif c in alphabet_ru:
#                 s1 += alphabet_ru[(alphabet_ru.find(c) - k) % 32]
#             else:
#                 s1 += c
#     elif language.lower() == 'английский':
#         for c in s:
#             if c in alphabet_EN:
#                 s1 += alphabet_EN[(alphabet_EN.find(c) - k) % 26]
#             elif c in alphabet_en:
#                 s1 += alphabet_en[(alphabet_en.find(c) - k) % 26]
#             else:
#                 s1 += c
# print(s1)



# alphabet_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
# st = input().split()
# lst = []
# # st1 = ''
# for i in st:
#     st1 = ''
#     n = 0
#     for j in i:
#         if j.isalpha():
#             n += 1
#     for c in i:
#         if c in alphabet_EN:
#             st1 += alphabet_EN[(alphabet_EN.find(c) + n) % 26]
#         elif c in alphabet_en:
#             st1 += alphabet_en[(alphabet_en.find(c) + n) % 26]
#         else:
#             st1 += c
#     lst.append(st1)
# print(*lst)


# def calculator(b, n):
#     if b != 16:
#         return sum([int(n[-1 - i]) * b**i for i in range(len(n))])
#     else:
#         s = list()
#         for i in range(len(n)):
#             if n[-1 - i] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
#                 s.append(int(n[-1 - i]) * b**i)
#             else:
#                 s.append((ord(n[-1 - i]) - 55) * b**i)
#         return sum(s)
#
#
# print('Вас приветствует калькулятор переводчик из какой-то случайной сс в десятичную сс.')
# while True:
#     print('Введите основание сс, а затем само число.')
#     base, number = int(input()), input()
#     print('Результат в десятичной сс =', calculator(base, number))
#     output = input('Если желаете покинуть программу, просто напишите EXIT и нажмите ENTER\nВ противном случае нажмите ENTER\n')
#     if output == 'EXIT':
#         break


# print(int('1AF2', 16))

# num10 = int(input())
# print(str(bin(num10))[2:])
# print(str(oct(num10))[2:])
# print(str(hex(num10))[2:].upper())
