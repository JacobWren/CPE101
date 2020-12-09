# Name: Jacob Wren
# Course: CPE 101
# Instructor: Irene Humer
# Assignment: Problem seta
# Term: Winter 2020

import pseta

assert pseta.count_zeros([1, 2, 0, 0, 0]) == 3
assert pseta.count_zeros([1, 2, 0]) == 1
assert pseta.count_zeros([1, 2]) == 0

assert pseta.try_isalnum('a!') == False
assert pseta.try_isalnum('ab1') == True
assert pseta.try_isalnum('2') == True
assert pseta.try_isalnum('!') == False
assert pseta.try_isalnum('1212') == True
assert pseta.try_isalnum('3abc') == True
assert pseta.try_isalnum('3abc!') == False

assert pseta.get_numeric_type(1) == 'int'
assert pseta.get_numeric_type(1.1) == 'float'
assert pseta.get_numeric_type(1.2) == 'float'
assert pseta.get_numeric_type(10) == 'int'

assert pseta.get_sequence_type('jake') == "str"
assert pseta.get_sequence_type('') == "str"
assert pseta.get_sequence_type((1, 1)) == "tuple"
assert pseta.get_sequence_type([1]) == "list"
assert pseta.get_sequence_type([]) == "list"

assert pseta.are_same_type('j', 'l') == True
assert pseta.are_same_type(None, None) == True
assert pseta.are_same_type([1], []) == True
assert pseta.are_same_type((1, 1), (1, 2, 3)) == True
