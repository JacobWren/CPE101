# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020



def reverse_string(chars, index):
    if len(chars) == 0:
        return None
    if index + 1 == len(chars):
        return chars[index]
    index = index + 1
    return reverse_string(chars, index) + chars[index - 1]


def is_palindrome(chars, index):
    if index == len(chars):
        return True
    if chars[index] == chars[1 - index -1]:
        index = index + 1
        return is_palindrome(chars, index)
    else:
        return False


def find_max(ints, index):
    if index == len(ints) - 1:
        return ints[index]
    if find_max(ints, index + 1) > ints[index]:
        return find_max(ints, index + 1)
    else:
        return ints[index]


def mul(x, y):
    if y <= 0:
        return 0
    return x + mul(x, y - 1)


def exp(x, y):
    if y <= 0:
        return 1
    return mul(exp(x, y - 1), x)


def factorial(n):
    if n == 0:
        return 1
    return mul(factorial(n - 1), n)


def fibonacci(n, acc):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2, acc) + fibonacci(n - 1, acc)


def binary_search(ints, n, start, end):
    avg = (start + end) // 2
    if start == 0 and end == len(ints):
        end = len(ints) - 1
    if ints[avg] == n:
        return avg
    elif start == end:
        return -1
    if n > ints[avg]:
        return binary_search(ints, n, avg + 1, end)
    elif n < ints[avg]:
        return binary_search(ints, n, start, avg)
        
































    


