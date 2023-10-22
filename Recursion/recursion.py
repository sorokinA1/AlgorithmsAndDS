# https://www.youtube.com/watch?v=A3VQmxoWLHY
# https://www.youtube.com/watch?v=6oDQaB2one8
# если забыл, то codebeauty тема про бинарные деревья и рекурсию!

# def sum_num(n):
#     if n == 0:
#         return n
#     else:
#         return n + sum_num(n - 1)

# print(sum_num(5))

# def fact(n):
#     assert n >= 0 and int(n) == n, 'oops'
#     if n in [0, 1]:
#         return n
#     else:
#         return n * fact(n - 1)

# print(fact(2.4))

# def is_pal(s):
#     return len(s) < 2 or s[0] == s[-1] and is_pal(s[1:-1])

# print(is_pal('tenets'))

# def fib(n):
#     if n in [0, 1]:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 1)


# print(fib(5))

# def sum_num(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum_num(arr[1:])

# print(sum_num([1, 2, 3]))

# def rev(s):
# if len(s) == 1:
#     return s[0]
# else:
#     return s[-1] + s[:-1]

# print(rev('abc'))

# def sum_arr(arr):
#     res = []
#     for el in arr:
#         if type(el) == list:
#             res.extend(sum_arr(el))
#         else:
#             res.append(el)
#     return res

# print(sum_arr([0, 1, 2, [2, 4, 5, [6, [7, 8, [9]]]]]))


# def capital(list: list):
#     if len(list) == 0:
#         return []
#     else:
#         return [list[0].upper()] + capital(list[1:])


# print(capital(['foo', 'bar', 'world', 'hello']))

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# def my_func(arr, func):
#     if len(arr) == 0:
#         return False
#     if func(arr[0]):
#         return True

#     return my_func(arr[1:], func)


# print(my_func([2, 4, 6], isEven))
# print(my_func([1, 7, 3, 5], isEven))

# def sum_num(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum_num(arr[1:])

# print(sum_num([1, 2, 3]))

# def sum_num(arr):
#     res = 0
#     for el in arr:
#         if type(el) == list:
#             res += sum_num(el)
#         else:
#             res += el
#     return res

# print(sum_num([1, 2, [3, 4], [5, 6]]))


# def sum_num(n):
#     if n == 0:
#         return n
#     else:
#         return n % 10 + sum_num(int(n / 10))

# print(sum_num(421))

# def pow(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * pow(x, n - 1)


# print(pow(3, 4))

# def bin(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * bin(int(n / 2))


# print(bin(10))


# def sum_num(n):
#     if n in [0, 1]:
#         return n
#     else:
#         return n + sum_num(n - 1)

# print(sum_num(10))

# def fact(n):
#     assert n >= 0 and int(n) == n, 'oops'
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * fact(n - 1)


# print(fact(5))

# def fib(n):
#     assert n >= 0 and int(n) == n
#     if n in [0, 1]:
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)


# print(fib(10))

# def sum_el(arr):
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum_el(arr[1:])

# print(sum_el([1, 2, 3]))


# def mul_el(arr):
#     if len(arr) == 0:
#         return 1
#     else:
#         return arr[0] * mul_el(arr[1:])


# print(mul_el([1, 2, 3, 4]))

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 0
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[len(arr)-1] * productOfArray(arr[:len(arr)-1])


# print(productOfArray([1, 2, 3, 4]))

# def is_pal(s):
#     return len(s) < 2 or s[0] == s[-1] and is_pal(s[1:-1])


# print(is_pal('tenet'))


# def rev(s):
#     print(s)
#     if len(s) == 1:
#         return s[0]
#     else:
#         return s[-1] + rev(s[:-1])

# print(rev('amazing'))

# def flat_arr(arr):
#     res = []

#     for el in arr:
#         if type(el) == list:
#             res.extend(flat_arr(el))
#         else:
#             res.append(el)

#     return res


# print(flat_arr([0, [1], [2, 3], [4], [3, [2, 4, [5, 6, [7, 8, [9]]]]]]))


# def cap_words(arr):
#     if len(arr) == 0:
#         return []

#     return [arr[0].upper()] + cap_words(arr[1:])


# print(cap_words(['foo', 'bar', 'world', 'hello']))

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# def some_func(arr, func):
#     if len(arr) == 0:
#         return False
#     if func(arr[-1]):
#         return True

#     return some_func(arr[:-1], func)


# print(some_func([1, 2, 3, 5], isEven))


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# def check_even(arr, func):
#     if len(arr) == 0:
#         return False
#     if func(arr[0]):
#         return True

#     return check_even(arr[1:], func)


# print(check_even([1, 7, 3, 5], isEven))

# def sum_el(arr):
#     print(arr[0], arr)
#     if len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum_el(arr[1:])


# print(sum_el([1, 2, 3]))

# def sum_el(arr):
#     res = 0

#     for el in arr:
#         if type(el) == list:
#             res += sum_el(el)
#         else:
#             res += el

#     return res

# print(sum_el([1, 2, [3, 4], [5, 6, [7, 8, [9]]]]))

# def fact(n):
#     assert n >= 0 and int(n) == n
#     if n in [0, 1]:
#         return n
#     else:
#         return n * fact(n - 1)


# print(fact(5))

# def sum_num(n):
#     assert n >= 0 and int(n) == n
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_num(int(n / 10))


# print(sum_num(421))


# def pow(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * pow(x, n - 1)


# print(pow(2, 5))

# def bin(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * bin(int(n / 2))


# print(bin(10))

# def gcd(a, b):
#     assert a == int(a)
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)


# print(gcd(48, 18))


# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         gcd(b, a % b)

#################################################################################
#################################################################################
#################################################################################
#################################################################################

# def sum_num(n):
#     if n == 0:
#         return n
#     else:
#         return n + sum_num(n - 1)
# print(sum_num(3))

# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return int(n / 10) + (n % 10)
#
# print(sum_of_digits(54))

# def power(n, pow):
#     if pow == 0:
#         return 1
#     else:
#         return n * power(n, pow - 1)
#
#
# print(power(3, 4))

# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)
#
#
# print(gcd(64, 48))

# def bin(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 2 + 10 * bin(int(n / 2))
#
#
# print(bin(10))
