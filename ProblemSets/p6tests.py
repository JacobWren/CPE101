# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Pset6
# Term:         Winter 2020

import pset6

assert pset6.poly_add([1, 2, 3], [2, 3, 4]) == [3, 5, 7]
assert pset6.poly_add([2, 3], [2, 3, 4]) == [4, 6, 4]
assert pset6.poly_add([0, 0, 0, 0], [2, 3, 4]) == [2, 3, 4, 0]

assert pset6.poly_mul([2, 1, 3], [4, 2, 1, 2]) == [8, 8, 16, 11, 5, 6]
assert pset6.poly_mul([1, 3, 2, 2], [0, 1, 1]) == [0, 1, 4, 5, 4, 2]
assert pset6.poly_mul([0], [2, 1, 1, 0, 0, 0, -1]) == [0]

assert pset6.get_mode([2, 1, 3]) == 2
assert pset6.get_mode([1]) == 1
assert pset6.get_mode([1, 3, 2, 2]) == 2
assert pset6.get_mode([1, 3, 2, 2]) == 2
assert pset6.get_mode([1, 1, 1, 3, 2, 2]) == 1
assert pset6.get_mode([1, 1, 3, 2]) == 1

assert pset6.index_of_smallest([2, 1, 3]) == 1
assert pset6.index_of_smallest([]) == -1
assert pset6.index_of_smallest([8, 3, 2, 2]) == 2
assert pset6.index_of_smallest([5, 4, 3, 2, 1]) == 4
assert pset6.index_of_smallest([1, 9, 3, 1]) == 0
assert pset6.index_of_smallest([0, 0, 0, 1]) == 0
assert pset6.index_of_smallest([1]) == 0
assert pset6.index_of_smallest([0, 0, 0, 1]) == 0

assert pset6.has_duplicates([1, 0, 2, 0, 3]) == False
assert pset6.has_duplicates([]) == False
assert pset6.has_duplicates([1, 2, 3, 2, 4]) == True

assert pset6.products([[1, 2, 3], [4, 5], [-10], []]) == [6, 20, -10, 0]
assert pset6.products([[]]) == [0]
assert pset6.products([[1, 2, 5], [4, 5], [-10], []]) == [10, 20, -10, 0]

assert pset6.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert pset6.fibonacci(0) == []
assert pset6.fibonacci(3) == [0, 1, 1]
assert pset6.fibonacci(1) == [0]
assert pset6.fibonacci(2) == [0, 1]

assert pset6.geo_mean([4, 4, 4, 4]) == 4.0
assert pset6.geo_mean([0]) == 0.0
assert pset6.geo_mean([1, 9]) == 3.0
assert pset6.geo_mean([]) == 0

assert pset6.harmonic_mean([4, 7, 9, 3]) == 4.777251184834124
assert pset6.harmonic_mean([4, 7, 9]) == 5.952755905511811
assert pset6.harmonic_mean([4]) == 4.0
assert pset6.harmonic_mean([]) == 0
assert pset6.harmonic_mean([0]) == 0
assert pset6.harmonic_mean([2, -1, 2]) == 2.0
assert pset6.harmonic_mean([2, -1, 2]) == 2.0

assert pset6.nest_lists(1) == []
assert pset6.nest_lists(2) == [[]]
assert pset6.nest_lists(3) == [[[]]]

assert pset6.solve_bool_exp(["not", "X", "or" , "Y"], (True, False)) == False
assert pset6.solve_bool_exp(["X", "or" , "Y"], (True, False)) == True
assert pset6.solve_bool_exp(["not", "X", "and" , "not", "Y"], (True, False)) == False
assert pset6.solve_bool_exp(["X", "or" , "not", "Y"], (True, False)) == True
assert pset6.solve_bool_exp(["X", "and" , "not", "Y"], (True, False)) == True
