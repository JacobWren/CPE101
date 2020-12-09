# Name: Jacob Wren
# Course: CPE 101
# Instructor: Irene Humer
# Assignment: Problem set9
# Term: Winter 2020

import pset9

assert pset9.bubble_pass([4, 3, 1, 5, 2]) == [3, 1, 4, 2, 5]
assert pset9.bubble_pass([4, 3, 9, 2, 2]) == [3, 4, 2, 2, 9]
assert pset9.bubble_pass([4, 3, 1, 5, 0]) == [3, 1, 4, 0, 5]
assert pset9.bubble_pass([4]) == [4]

assert pset9.find_min([4, 3, 1, 5, 2]) == 1
assert pset9.find_min([4, 3, 9, 2, 2]) == 2
assert pset9.find_min([4, 3, 1, 5, 0]) == 0
assert pset9.find_min([3, 4, 1, 5, 2]) == 1
assert pset9.find_min([3]) == 3

assert pset9.selection_pass([4, 3, 1, 5, 0], 0) == [0, 3, 1, 5, 4]
assert pset9.selection_pass([4, 3, 1, 5, 2], 0) == [1, 3, 4, 5, 2]
assert pset9.selection_pass([4, 3, 1, 5, 6], 0) == [1, 3, 4, 5, 6]
assert pset9.selection_pass([1], 4) == [1]
assert pset9.selection_pass([], 0) == []

assert pset9.selection_pass([-6, 93, 7, 2, 99], 1) == [-6, 2, 7, 93, 99]
assert pset9.selection_pass([4, 7, 32, 6, 7, -1], 0) == [-1, 7, 32, 6, 7, 4]
assert pset9.selection_pass([6, 3, 88, 3213, 67], 100) == [6, 3, 88, 3213, 67]

assert pset9.insertion_pass([-6, 93, 7, 2, 99], 1) == [-6, 93, 7, 2, 99]
assert pset9.insertion_pass([4, 7, 32, 6, 7, -1], 0) == [4, 7, 32, 6, 7, -1]
assert pset9.insertion_pass([6, 3, 88, 3213, 67], 100) == [6, 3, 88, 3213, 67]
assert pset9.insertion_pass([4, 3, 2], 1) == [3, 4, 2]
assert pset9.insertion_pass([6, 3, 64, 2], 3) == [2, 6, 3, 64]

assert pset9.binary_search([1, 2, 3, 4, 5], 1) == 0
assert pset9.binary_search([1, 2, 3, 4, 5], 4) == 3
assert pset9.binary_search([1, 2, 3, 4, 5], 3) == 2
assert pset9.binary_search([1, 2, 3, 4, 5, 8, 9, 12, 1234], 1234) == 8
assert pset9.binary_search([1, 2, 3, 4, 5], 7) == -1
assert pset9.binary_search([1, 2, 3, 4, 5], 0) == -1
assert pset9.binary_search([1], 0) == -1

assert pset9.sort_ints([1, 2, 5, 4, 3], "bubble") == [1, 2, 3, 4, 5]
assert pset9.sort_ints([5, 2, 1, 4, 3], "bubble") == [1, 2, 3, 4, 5]
assert pset9.sort_ints([2], "selection") == [2]
assert pset9.sort_ints([2, 1, 3, 4, 5], "selection") == [1, 2, 3, 4, 5]
assert pset9.sort_ints([3, 2, 5, 4, 1], "insertion") == [1, 2, 3, 4, 5]
assert pset9.sort_ints([3], "insertion") == [3]                         
