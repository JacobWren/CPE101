# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020


import psetc


assert psetc.reverse_string('', 0) == None
assert psetc.reverse_string('jake', 0) == 'ekaj'
assert psetc.reverse_string('CalPoly', 0) == 'yloPlaC'


assert psetc.is_palindrome('', 0) == True
assert psetc.is_palindrome('jake', 0) == False
assert psetc.is_palindrome('CalPoly', 0) == False


assert psetc.find_max([2], 0) == 2
assert psetc.find_max([1, 2], 0) == 2
assert psetc.find_max([5, 2, 3], 0) == 5


assert psetc.mul(1, 2) == 2
assert psetc.mul(2, 2) == 4
assert psetc.mul(3, 2) == 6


assert psetc.exp(1, 2) == 1
assert psetc.exp(2, 2) == 4
assert psetc.exp(3, 2) == 9


assert psetc.factorial(0) == 1
assert psetc.factorial(1) == 1
assert psetc.factorial(2) == 2


assert psetc.fibonacci(1, (0, 1)) == 1
assert psetc.fibonacci(3, (0, 1)) == 2
assert psetc.fibonacci(2, (0, 1)) == 1


assert psetc.binary_search([1, 2], 1, 0, 1) == 0
assert psetc.binary_search([1, 2], 2, 0, 2) == 1
assert psetc.binary_search([1, 2, 3], 2, 0, 2) == 1
assert psetc.binary_search([1, 2, 3], 3, 0, 2) == 2
assert psetc.binary_search([1, 2, 3, 4], 8, 0, 4) == -1
assert psetc.binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 0, 10) == 7
assert psetc.binary_search([11, 19, 34, 50, 67, 89], 13, 0, 10) == -1







