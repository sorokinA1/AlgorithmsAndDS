# word = 'amazing'
#
# def rev(text):
#     if len(text) == 1:
#         return text[0]
#     return text[-1] + rev(text[:-1])
#
#
# def count_down_from(number):
#     if number == 0:
#         return 0
#     print(number)
#     return count_down_from(number - 1)


# classes = ['druid', 'warrior', 'mage', 'rogue']
#
# for item in enumerate(classes):
#     # print(item)
#     if 'warrior' in classes:
#         print(f'found {item[1]} at {item[0]}')

# label = 'Steak and Potatoes'

# for char in label:
#     print(char, '-')

# num_list = [5, 10, 15, 20, 25, 30]
#
#
# def odd_numbers_sum(numbers: list) -> int:
#     result = 0
#     for i in numbers:
#         if i % 2 == 1:
#             result += i
#     return result
#
#
# print(odd_numbers_sum(num_list))

# the_simpsons = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']
#
# for i in the_simpsons[::-1]:
#     print(len(i), i)
#
# print(reversed(the_simpsons))
#
# for i in reversed(the_simpsons):
#     print(i)

# the_simpsons = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']
#
# for i, el in enumerate(the_simpsons, 1):
#     print(f'{i}:', el)

# nums = []
#
# for i in range(11):
#     nums.append(i)
#
# print('finished')

# swapping
# coworkers = ['Michael', 'Jim', 'Pam', 'Dwight', 'Creed', 'Angela']
#
# coworkers[0], coworkers[1] = coworkers[1], coworkers[0]
#
# coworkers[3:5] = ['Oscar', 'Ryan']
# print(coworkers)

# coworkers = ['Michael', 'Jim', 'Pam', 'Dwight', 'Creed', 'Angela']
#
# new_peps = ['Sayaka', 'Kyoko']
#
# coworkers.extend(new_peps)
#
# print(coworkers)

# action_starts = ['Norris', 'Seagal', 'Van Damme', 'Scharznegger']
#
# action_starts.pop()
# action_starts.pop(1)


# vitamins = ['A', 'D', 'K']
# vitamins.reverse()
# print(vitamins)

# temperatures = [40, 28, 52, 66, 35]
# temperatures.sort()
# print(temperatures)

# ext_data = 'some text { som dict { some dict { some value } } }'
# print(ext_data.count('{'))

# string = 'comma,separated,string'
#
# x = string.split(',')
# print(x)
#
# names = ['Sayaka', 'Jun', 'Kyoko']
# y = ', '.join(names)
# print(y)

# classes = ['warrior', 'rogue', 'hunter']
# dps = [3000, 2700, 1600]
# gear = [49, 34, 24]
#
# mapping_class_dps = zip(classes, dps, gear)
#
# print(mapping_class_dps)
#
# for i in zip(classes, dps, gear):
#     print(i)

# rotate matrix
# image = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# [1, 4, 7]
# [2, 5, 0]
# [6, 8, 9]


# def rotate(matrix):
#     matrix.reverse()
#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#
# rotate(image)
# print(image)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)


# list comprehension

# numbers = [3, 4, 5, 6, 7]
# new_nums = [i for i in numbers if i % 2 == 0]
# print(new_nums)
#
# rivers = ['Amazon', 'Nile', 'Yangtze']
#
# rivers_length = [len(river) for river in rivers]
# print(rivers_length)


# maps
# my_nums = [1, 2, 3, 4, 5]
#
# rivers = ['Amazon', 'Nile', 'Yangtze']
#
# nums_2 = list(map(lambda num: num * 2, my_nums))
#
# rivers_upper = list(map(lambda river: river.upper(), rivers))
# print(rivers_upper)


# print(['abcdefghijklmnopqrstuvwxyz'.index(char) for char in 'donut'])
# print([number / 2 for number in range(21)])

# donuts = [
#     'Boston cream',
#     'Jelly',
#     'Glazed',
#     'Chocolate cream'
# ]
#
# donuts_with_cream = [donut for donut in donuts if 'cream' in donut]
# print(donuts_with_cream)


# tup = (1, 2)
# print(type(tup))

# binary search
# arr = [11, 23, 37, 41, 56, 62, 79, 83, 92]
#
# def binary_search(data, target):
#     left = 0
#     right = len(data) - 1
#
#     while left <= right:
#         mid_point = (left + right) // 2
#
#         if data[mid_point] > target:
#             right = mid_point - 1
#         elif data[mid_point] < target:
#             left = mid_point + 1
#         else:
#             return mid_point
#
#     return -1
#
#
# print(binary_search(arr, 79))


# employee = ('Bob', 'Johnson', 'Manager', 50)
#
# first_name, last_name, position, age = employee
#
# print(first_name, last_name, position, age)
# print(employee[0], employee[1])
#
# text = ['python', 'is', 'fun']
#
# a = 5
# b = 7
#
# a, b = b, a
#
# print('a', a)
# print('b', b)

# employee = ('Bob', 'Johnson', 'Manager', 50)
#
# first_name, last_name, *details = employee
#
# print(first_name, last_name, details)
#
# *names, position, age = employee
# print(names, position, age)

# *args

# def sum_of_nums(*args):
#     return sum(args)
#
# print(sum_of_nums(1, 2, 3, 4, 5))

# def my_max(nonsense, *args):
#     print(nonsense)
#     print(args)
#     # greatest = args[0]
#     # for i in args:
#     #     if i > greatest:
#     #         greatest = i
#     # return greatest
#
#
# print(my_max('hi', 2, 4, 5, 6, 7, 10, 6, 4))


# def product(a, b):
#     return a * b
#
# numbers = [3, 5]
#
# print(product(*numbers))

# icecream_preferences = {
#     'Sayaka': 'Vanilla',
#     'Jun': 'Chocolate',
#     'Kyoko': 'Strawberry'
# }
#
# print(icecream_preferences.get())
# print(icecream_preferences.values())

# gym_membership_packages = {
#     29: ['Machines'],
#     49: ['Machines', 'Vitamins'],
#     79: ['Machines', 'Vitamins', 'Sauna'],
# }

# print(gym_membership_packages.get(39, 'not found'))
# print(gym_membership_packages.values())

# if 'Sauna' in gym_membership_packages.values():
#     print('hi')
# else:
#     print('not found')

# sports_team_roaster = {
#     'New England Patriots': ['Tom Brady', 'Rob Gronowski', 'Julian Edleman'],
#     'New York Giants': ['Eli Manning', 'Odell Beckham']
# }
#
# sports_team_roaster['Pittburg Steelers'] = ['Ben Roethliberger', 'Antonio Brown']
# sports_team_roaster['Pittburg Steelers'] = ['Ben Roethliberger']
# print(sports_team_roaster['Pittburg Steelers'])

# words = ['danger', 'beware', 'danger']
#
#
# def count_words(words):
#     all_words = { }
#     for word in words:
#         if word not in all_words:
#             all_words[word] = 1
#         else:
#             all_words[word] += 1
#
#     return all_words
#
#
# print(count_words(words))

# film_directors = {
#     'The GodFather': 'Ford Capola',
#     'The Rock': 'Michael Bay',
#     'Goodfellas': 'Martin Scoreee'
# }
#
# print(film_directors.setdefault('Bad boys', 'Michael Bay'))
# print(film_directors.setdefault('Bad boys', 'Michael Bay'))
#
# print(film_directors)


# [10, 20, 30, 40, 50, 60, 70]

# def binary_search(data, target):
#     left = 0
#     right = len(data) - 1
#
#     while left <= right:
#         mid_point = (left + right) // 2
#
#         if target < data[mid_point]:
#             right = mid_point - 1
#         elif target > data[mid_point]:
#             left = mid_point + 1
#         else:
#             return mid_point
#
#     return -1
#
#
# numbers = [5, 6, 15, 25, 45, 145]
#
# print(binary_search(numbers, 45))


# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self, head=None, end=None):
#         self.head = head
#         self.end = end
#
#     def display(self):
#         if self.head is None:
#             print('[]')
#         else:
#             elements = []
#             cur_node = self.head
#
#             while cur_node:
#                 elements.append(cur_node.data)
#                 cur_node = cur_node.next
#                 if cur_node == self.head:
#                     break
#             print(elements)
#
#
#     def length(self):
#         count = 0
#         cur_node = self.head
#
#         while cur_node:
#             count +=1
#             cur_node = cur_node.next
#             if cur_node == self.head:
#                 break
#         return count
#
#
#     def push(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             self.head.next = new_node
#             self.end = new_node
#         else:
#             self.end.next = new_node
#             new_node.next = self.head
#             self.end = new_node

# languages = ['Python', 'Ruby', 'JavaScript']
#
# lang_dict = { language: len(language) for language in languages if len(language) > 4 }
# print(lang_dict)
#
# word = 'supercalifragilisticxpialidocious'
#
# letters = { letter: word.count(letter) for letter in word }
# print(letters)


# def collect_kwargs(**kwargs):
#     print(kwargs)
#
#
# collect_kwargs(a=2, b=3, c=4)
#
#
# def args_and_kwargs(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
#
#
# args_and_kwargs('hi', 'there', 1, 2, 3, 4, 5, warrior=9000)

# def height_to_meters(feet, inches):
#     total_inches = (feet * 12) + inches
#     return total_inches * 0.0254
#
#
# print(height_to_meters(5, 11))
#
# height = {
#     'feet': 5,
#     'inches': 11
# }
#
# print(height_to_meters(**height))


# capitals = {
#     'New York': 'Albany',
#     'California': 'Sacramento',
#     'Texas': 'Austin'
# }
#
# capitals_to_states = { capitals[capital]: capital for capital in capitals }
# print(capitals_to_states)

# my_dict = {
#     'Spider': 'photographer',
#     'Batman': 'philanthropist',
#     'Wonder Wo': 'nurse'
# }
#
# full_names = { key + 'man': val for key, val in my_dict.items() }
# print(full_names)

# mr_freeze = frozenset([1, 2, 3, 2, 1])
# print(mr_freeze)

# def create_cubes(n):
#     return [x ** 3 for x in range(n)]

# def create_cubes(n):
#     for x in range(n):
#         yield x ** 3
#
#
# for x in create_cubes(10):
#     print(x)


# import feature.subfeature.calculator
# from feature.subfeature import calculator

# import feature
#
# print(feature.add(2, 3))


# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def calculate(a, b, func):
#     return func(a, b)
#
#
# print(calculate(2, 3, add))
# print(calculate(3, 1, subtract))

# Gallons to cups

# 1 gallon = 4 quarts
# 1 quart = 2 pints
# 1 pint = 2 cups

# def convert_gallons_to_cups(gallons):
#     def gallons_to_quarts(gallons):
#         print(f'Converting {gallons} gallons to quarts!')
#         return gallons * 4
#
#     def quarts_to_pints(quarts):
#         print(f'Converting {quarts} quarts to pints')
#         return quarts * 2
#
#     def pints_to_cups(pints):
#         print(f'Converting {pints} quarts to pints')
#         return pints * 2
#
#     quarts = gallons_to_quarts(gallons)
#     pints = quarts_to_pints(quarts)
#     return pints_to_cups(pints)
#
#
# print(convert_gallons_to_cups(1))

# def calculator(operation):
#     def add(a, b):
#         return a + b
#
#     def subtract(a, b):
#         return a - b
#
#     if operation == 'add':
#         return add
#
#     elif operation == 'subtract':
#         return subtract
#
#
# print(calculator('add')(2, 3))
# print(calculator('subtract')(3, 2))

# x = 0
#
# def outer():
#     # x = 10
#
#     def inner():
#         # x = 5
#         return len
#
#     return inner()
#
#
# print(outer()('Python'))

# def outer():
#     candy = 'snickers'
#
#     def inner():
#         return candy
#
#     return inner
#
#
# the_func = outer()
#
# print(the_func())

# x = 10
#
# def change_stuff():
#     global x
#     x = 15
#
# change_stuff()
#
# print(x)

# def outer():
#     bubble_tea_flavor = 'black tea'
#
#     def inner():
#         nonlocal bubble_tea_flavor
#         bubble_tea_flavor = 'taro'
#
#     inner()
#
#     return bubble_tea_flavor
#
#
# print(outer())


# def be_nice(fn):
#     def inner():
#         print('Nice to meet you')
#         fn()
#         print('the function was executed')
#
#     return inner
#
#
# @be_nice
# def complex_business_logic():
#     print('Something complex')
#
#
# complex_business_logic()


# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print(f'Nice to meet you')
#         fn(*args, **kwargs)
#         print('the function was executed')
#
#     return inner
#
#
# @be_nice
# def complex_business_logic(stakeholder, position):
#     print(f'Something complex for {position} {stakeholder}')
#
#
# complex_business_logic('Sayaka', position='CEO')


# def be_nice(fn):
#     def inner(*args, **kwargs):
#         print(f'Nice to meet you')
#         result = fn(*args, **kwargs)
#         print('the function was executed')
#         return result
#
#     return inner
#
#
# @be_nice
# def complex_business_sum(a, b):
#     return a + b
#
# print(complex_business_sum(2, 3))

# class Person:
#     def __init__(self, name='Unnamed', age=0):
#         self.name = name
#         self.age = age
#
#
# sayaka = Person(age=20)
#
# print(sayaka.name)

# class Height:
#     def __init__(self, feet):
#         self.inches = feet * 12
#
#     def _get_feet(self):
#         return self.inches / 12
#
#     def _set_feet(self, feet):
#         if feet >= 0:
#             self.inches = feet * 12
#
#     feet = property(_get_feet, _set_feet)
#
#
# h = Height(5)
# h.feet = 3
# print(h.feet)

# class Currency:
#     def __init__(self, dollars):
#         self._cents = dollars * 100
#
#     @property
#     def dollars(self):
#         return self._cents / 100
#
#     @dollars.setter
#     def dollars(self, dollars):
#         if dollars >= 0:
#             self._cents = dollars * 100
#
#
# money = Currency(5000)

# 1  -3  5  -6  -10  13


# stop_counter = None
# all_nums = []
#
# while stop_counter != 0:
#     user_input = int(input())
#     if stop_counter is None:
#         stop_counter = user_input
#         all_nums.append(user_input)
#     else:
#         stop_counter += user_input
#         all_nums.append(user_input)
#
# for i in all_nums:
#     stop_counter += i ** 2
#
# print(stop_counter)

# number_of_digits_to_print = input()
# input_as_string = [str(i) for i in range(1, int(number_of_digits_to_print) + 1)]
# all_nums = ''
#
# i = 1
# for item in input_as_string:
#     all_nums += item * i
#     i += 1
#
# print(' '.join(all_nums[0: int(number_of_digits_to_print)]))
# print(len(' '.join(all_nums[0: int(number_of_digits_to_print)])))
#
#
# n = int(input())
# v = []
#
# for i in range(1, n + 1):
#     v += [str(i)] * i
#
# print(" ".join(v[:n]))


# list_of_numbers = input()
# number_to_find = input()
# filtered_list = [i for i in list_of_numbers if i != ' ']
# result = [int(i) for i, el in enumerate(filtered_list) if el == number_to_find]
# result.sort()
#
# if len(result) == 0:
#     print('Отсутствует')
# else:
#     print(' '.join([str(i) for i in result]))


# number_one = int(input())
# number_two = int(input())
#
# all_nums = [i for i in range(number_one, number_two + 1) if i % 3 == 0]
#
# print(sum(all_nums) / len(all_nums))


# user_input = input()
# char_counter = 0
#
# for i in user_input:
#     if i.lower() == 'g' or i.lower() == 'c':
#         char_counter += 1
#
# print((char_counter / len(user_input)) * 100)

# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)

# user_input = input().split()
# input_as_numbers = [int(i) for i in user_input]
# print(sum(input_as_numbers))

# user_input = input().split()
# input_as_numbers = [int(i) for i in user_input]
# result = []
#
# if len(input_as_numbers) == 1:
#     print(input_as_numbers[0])
# else:
#     i = 0
#     while i != len(user_input) - 1:
#         main_pointer = input_as_numbers[i]
#         left_pointer = input_as_numbers[i - 1]
#         right_pointer = input_as_numbers[i + 1]
#
#         result.append(left_pointer + right_pointer)
#         i += 1
#     result.append(input_as_numbers[-2] + input_as_numbers[0])
#
#     print(' '.join([str(i) for i in result]))


# user_input = input().split()
# input_as_numbers = [int(i) for i in user_input]
#
# result_dict = { }
# result_list = []
#
# for char in input_as_numbers:
#     if char not in result_dict:
#         result_dict[char] = 1
#     else:
#         result_dict[char] += 1
#
# for key, val in result_dict.items():
#     if val > 1:
#         result_list.append(key)
#
# print(' '.join([str(i) for i in result_list]))

# n = ''
# m = []
# while True:
#     n = str(input())  # ввод строк
#     if n == 'end':
#         break
#     m.append([int(s) for s in n.split()])
# li, lj = len(m), len(m[0])
# new = [[sum([m[i - 1][j], m[(i + 1) % li][j], m[i][j - 1], m[i][(j + 1) % lj]]) for j in range(lj)] for i in range(li)]
#
# for i in range(li):
#     for j in range(lj):
#         print(new[i][j], end=' ')
#     print()

# matrix = []
#
# while True:
#     user_input = input().split()
#     if 'end' in user_input:
#         break
#
#     matrix.append(int(i) for i in user_input)
#
# row_length = len(matrix)
# column_length = len(matrix[0])
#
# for i in range(row_length):
#     for j in range(column_length):
#         print(matrix[i][j - column_length + 1] + matrix[i][j - 1] + matrix[i - row_length + 1][j] + matrix[i - 1][j],
#               end=' ')
# https://www.youtube.com/watch?v=Y8cokWekOAo&t=234s


# user_input = [1, 2, 3, 4, 5, 6]
#
#
# # filtered_input = [int(i) // 2 for i in user_input if i % 2 == 0]
#
#
# def modify_list(l):
#     r = [int(i) // 2 for i in l if i % 2 == 0]
#     print(r)
#
#
# modify_list(user_input)

# def modify_list(l):
#     le = len(l)-1
#     i = le
#     while i!=-1:
#         if l[i]%2:
#             del l[i]
#         else:
#             l[i]=l[i]//2
#         i -=1
#     return


# [01, 02, 03, 04, 05]
# [06, 07, 08, 09, 10]
# [11, 12, 13, 14, 15]
# [16, 17, 18, 19, 20]
# [21, 22, 23, 24, 25]

# matrix_size = int(input())
#
# matrix_copy = [[None]* matrix_size for j in range(matrix_size)]
#
# result = matrix_copy
#
# start = 1
# end = matrix_size + 1
#
# for i in range(matrix_size):
#     matrix_copy.append([i for i in range(start, end)])
#     start = end
#     end += matrix_size

# https://www.cyberforum.ru/python-beginners/thread1580205.html

# n = int(input())
#
# # Создаем нулевую квадратную матрицу заданной размерности
# a = [[0 for i in range(n)] for j in range(n)]
#
# # Определяем внутренние счетчики для цикла
# i = 0  # строки
# j = 0  # столбцы
# x = 1  # текущее значение для заполнения ячейки
# k = 0  # порядковый номер контура
#
# while x <= n * n:
#     a[i][j] = x  # заполняем ячейку текущим значением
#
#     if i != j:  # Только если мы сейчас не на диагонали!
#         # Сумма зеркально расположенных элементов одинакова для текущего контура.
#         # Она равна нижнему правому значению в контуре, умноженному на 2.
#         # Так что на каждом шаге цикла мы заполняем зеркальный элемент матрицы,
#         # просто вычитая текущее x из этой суммы ;)
#         a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
#
#     if j != n - k - 1:
#         # если еще не уперлись в правую границу контура, двигаемся вправо
#         j += 1
#
#     elif i != n - k - 1:
#         # если еще не уперлись в нижнюю границу контура, двигаемся вниз
#         i += 1
#
#     elif x != n * n:
#         # Если вправо и вниз уже нельзя, значит мы закончили обход текущего контура!
#         # Только не забываем проверить, что x не равен n*n, а то будет бо-бо.
#         k += 1  # переходим к следующему контуру
#         i = j = k  # обход следующего контура начнем с координат [k,k]
#         x = a[k][k - 1]  # текущее значение равно наибольшему в старом контуре
#
#     x += 1  # Ну, и не забываем прибавлять единичку в конце цикла, какое бы условие ни сработало.
#
# # Выводим на печать
# for i in a: print(*i)

############################################
############################################
############################################
############################################
############################################
############################################

# n = int(input())
#
# a = [[0 for i in range(n)] for j in range(n)]
#
# i = 0
# j = 0
# x = 1
# k = 0
#
# while x <= n * n:
#     a[i][j] = x
#
#     if i != j:
#         a[j][i] = (a[k][k] + (n - k * 2) * 2) * 2 - 4 - x
#
#     if j != n - k - 1:
#         j += 1
#
#     elif i != n - k - 1:
#         i += 1
#
#     elif x != n * n:
#         k += 1
#         i = j = k
#         x = a[k][k - 1]
#
#     x += 1
# for i in a: print(*i)

# маска числа
# https://www.youtube.com/watch?v=CTFRfts19rQ

# Spiral matrix

# n = int(input())
#
# matrix = [[0] * n for _ in range(n)]
#
# left = 0
# right = n - 1
#
# top = 0
# bottom = n - 1
#
# val = 1
#
# while left <= right:
#
#     # fill every val in top row
#     for column in range(left, right + 1):
#         matrix[top][column] = val
#         val += 1
#     top += 1
#
#     # fill every val in right col
#     for row in range(top, bottom + 1):
#         matrix[row][right] = val
#         val += 1
#     right -= 1
#
#     # fill every val in bottom row (reverse)
#     for column in range(right, left - 1, -1):
#         matrix[bottom][column] = val
#         val += 1
#     bottom -= 1
#
#     # fill every val in left col (reverse)
#     for row in range(bottom, top - 1, -1):
#         matrix[row][left] = val
#         val += 1
#     left += 1

# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif d[key] not in d:
#         d[key * 2].append(value)
#     elif d[key * 2] not in d:
#         d[key * 2] = [value]

# new_input = input().split()
# result = { }
#
# for letter in new_input:
#     if letter.lower() not in result:
#         result[letter.lower()] = 1
#     else:
#         result[letter.lower()] += 1
#
# for key, val in result.items():
#     print(f'{key} {val}')


# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     else:
#         new_key = 2 * key
#         if new_key in d:
#             d[new_key].append(value)
#         else:
#
#             d[new_key] = [value]

# test_string = 'a12b10c3d1'

# digits = set('0123456789')
# i = 0
# multiplier = ''
# decrypted = ''
#
# with open('dataset_3363_2.txt') as in_f_obj:
#     string = in_f_obj.readline().strip()
#
# char = string[i]
# i += 1
#
# while i < len(string):
#
#     while string[i] in digits:
#         multiplier += string[i]
#         i += 1
#         if i > (len(string) - 1):
#             break
#
#     # print(char * int(multiplier), end='')
#     decrypted += (char * int(multiplier))
#
#     multiplier = ''
#     if i > (len(string) - 1):
#         break
#     char = string[i]
#
#     i += 1
#
# with open('03_04_02_ouput.txt', 'w') as out_f_obj:
#     out_f_obj.write(decrypted)


# with open('dataset_3363_3.txt') as in_f_obj:
#     string = in_f_obj.readline().strip().split()
#
# result = { }
# most_often_used_word = { }
#
# for letter in string:
#     if letter.lower() not in result:
#         result[letter.lower()] = 1
#     else:
#         result[letter.lower()] += 1
#
# max_val = 1
# for key, val in result.items():
#     if val > max_val:
#         max_val = val
#
# for key, val in result.items():
#     if val == max_val:
#         most_often_used_word[key] = val
#
# with open('03_04_02_ouput.txt', 'w') as out_f_obj:
#     for key, val in most_often_used_word.items():
#         print(f'{key} {val}')
#         out_f_obj.writelines(f'{key}{val} ')

# dictionary = { }
#
# with open('dataset_3363_3.txt') as in_f_obj:
#     for line in in_f_obj:
#         line = line.lower()
#         for word in line.split():
#             if word not in dictionary:
#                 dictionary[word] = 1
#             elif word in dictionary:
#                 dictionary[word] += 1
#
# max_quantity = 1
#
# for key, value in dictionary.items():
#     current_quantity = dictionary[key]
#     if current_quantity > max_quantity:
#         max_quantity = current_quantity
#         word_with_max_quantity = key
#
# with open('03_04_03_output.txt', 'w') as out_f_obj:
#     most_popular = (word_with_max_quantity + ' ' + str(max_quantity))
#     out_f_obj.write(most_popular)


# math_values = []
# physics_values = []
# russian_values = []
# with open('dataset_3363_4.txt', 'r') as in_file:
#     for line in in_file:
#         current_line = line.strip().split(';')
#         math_values.append(int(current_line[1]))
#         physics_values.append(int(current_line[2]))
#         russian_values.append(int(current_line[3]))
# out_file = open('statistic.txt', 'w')
# for i in range(len(math_values)):
#     out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
# if len(math_values) > 0:
#     out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
#                    str(sum(physics_values) / len(physics_values)) + ' ' +
#                    str(sum(russian_values) / len(russian_values)))
# out_file.close()


# 8?321?
# 10**6 = 1000000
# 0123456789

# res = 0
#
# for i in '0123456789':
#     for j in '0123456789':
#         s = '8' + i + '321' + j
#
#         if int(s) % 5 == 0:
#             res += 1
#
# print(res)

# 8?321?

# from fnmatch import fnmatch
#
# k = 0
#
# for i in range(800000, 900000, 5):
#     s = str(i)
#     if fnmatch(s, '8?321?'):
#         k += 1
#
# print(k)

# 1000000
# 2738*

# k = 1
# # * = ''
# #  2738
# n = 2738
#
# if n % 7 == 0:
#     k += 1
#
# # * = '?'
# # 2738?
#
# for i in '0123456789':
#     s = '2738' + i
#     if int(s) % 7 == 0:
#         k += 1
#
# # * ='??'
# for i in '0123456789':
#     for j in '0123456789':
#         s = '2738' + i + j
#         if int(s) & 7 == 0:
#             k += 1
#
# print(k)


# 11ч??н11
# k = 0
#
# for x1 in '02468':
#     for x2 in '0123456789':
#         for x3 in '0123456789':
#             for x4 in '13579':
#                 s = '11' + x1 + x2 + x3 + x4 + '11'
#                 if int(s) % 2023 == 0:
#                     print(int(s), int(s) // 2023)

# 12345?7?8
# 100000000_0

# for i in '0123456789':
#     for j in '0123456789':
#         s = '12345' + i + '7' + j + '8'
#         if int(s) % 23 == 0:
#             print(int(s), int(s) // 23)


# import requests
#
# with open('dataset_3378_2.txt') as in_f_obj:
#     url = in_f_obj.read().strip()
#
# r = requests.get(url)
# counter = 0
#
# for line in r.text.splitlines():
#     counter += 1
#
# # Цикл выше можно заменить более простой конструкцией
# # print(len(r.text.splitlines()))
#
# with open('03_06_02_output.txt', 'w') as out_f_obj:
#     out_f_obj.write(str(counter))

# import requests
#
# link = 'https://stepic.org/media/attachments/course67/3.6.3/'
# with open('dataset_3378_3.txt') as inf:
#     t = inf.readline().strip()
#
# t = str(requests.get(t).text)
# while 'We' not in t:
#     print(t)
#     t = requests.get(link + t).text
# print(t)

# from requests import get
#
# r = get('https://stepik.org/media/attachments/course67/3.6.3/699991.txt')
# while r.text < 'We' or r.text >= 'Wf':
#     print(r.text)
#     r = get(url='http://stepic.org/media/attachments/course67/3.6.3/' + r.text.strip())
# print(r.text)

# table = []
# teams = {}
# points = 0
# match_count = 0
# victories = 0
# draws = 0
# losses = 0
#
# i = 0
#
# n = int(input())
#
# while i <= n - 1:
#     match = str(input())
#     table.append(match)
#     i += 1
#
# for i in range(len(table)):
#     table[i] = table[i].split(';')
#     teams[table[i][0]] = [match_count, victories, draws, losses, points]
#     teams[table[i][2]] = [match_count, victories, draws, losses, points]
#
#
# for i in range(len(table)):
#     table[i][1] = int(table[i][1])
#     table[i][3] = int(table[i][3])
#     if table[i][1] > table[i][3]:
#         teams[table[i][0]][0] += 1
#         teams[table[i][0]][1] += 1
#         teams[table[i][0]][4] += 3
#         teams[table[i][2]][0] += 1
#         teams[table[i][2]][3] += 1
#     elif table[i][1] < table[i][3]:
#         teams[table[i][2]][0] += 1
#         teams[table[i][2]][1] += 1
#         teams[table[i][2]][4] += 3
#         teams[table[i][0]][0] += 1
#         teams[table[i][0]][3] += 1
#     else:
#         teams[table[i][2]][0] += 1
#         teams[table[i][2]][2] += 1
#         teams[table[i][2]][4] += 1
#         teams[table[i][0]][0] += 1
#         teams[table[i][0]][2] += 1
#         teams[table[i][0]][4] += 1
#
# for fclub, stat in teams.items():
#     str_stat = list(map(str, stat))
#     print(fclub + ':' + ' '.join(str_stat))


# k = 0
# # 1?38?70*
# # * = ''
# for x in '0123456789':
#     for y in '0123456789':
#         string = '1' + x + '38' + y + '70'
#         if int(string) % 11 == 0:
#             k += 1
#
# # * = '?'
# for x in '0123456789':
#     for y in '0123456789':
#         for z in '0123456789':
#             string = '1' + x + '38' + y + '70' + z
#             if int(string) % 11 == 0:
#                 k += 1
#
# # * = '??'
# for x in '0123456789':
#     for y in '0123456789':
#         for z in '0123456789':
#             for c in '0123456789':
#                 string = '1' + x + '38' + y + '70' + z + c
#                 if int(string) % 11 == 0:
#                     k += 1
# print(k)

# def sum_all_numbers(number):
#     if number == 0:
#         return number
#     else:
#         return number + sum_all_numbers(number - 1)
#
#
# print(sum_all_numbers(5))

# def show_even_nums(number):
#     print(number)
#     if number <= 2:
#         return number
#     else:
#         return show_even_nums(number - 2)
#
#
# show_even_nums(9)

# 0, 1, 1, 2, 3, 5, 8, 13, 21

# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(3))

# def rev(s):
#     if len(s) == 1:
#         print(s)
#         return s[0]
#     else:
#         return s[-1] + rev(s[:-1])
#
#
# print(rev('amazing'))
#
# def is_pal(s):
#     return len(s) < 2 or s[0] == s[-1] and is_pal(s[1:-1])

# def is_palindrome(string):
#     return len(string) < 2 or string[0] == string[-1] and is_palindrome(string  [1:-1])

# 1000000000
# 1?38?70*

# * = ''
for x in '0123456789':
    for y in '0123456789':



