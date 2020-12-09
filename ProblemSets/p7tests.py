# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020


import pset7

assert pset7.get_reciprocals([1, 2, 3]) == [1, 1 / 2, 1 / 3]
assert pset7.get_reciprocals([0]) == []
assert pset7.get_reciprocals([1, 2, 0]) == [1, 1 / 2]


assert pset7.get_parities([-2, -1, 0, 1, 2]) == ["even", "odd", "even", "odd", "even"]
assert pset7.get_parities([-2]) == ["even"]
assert pset7.get_parities([-2, -1, 0, 1]) == ["even", "odd", "even", "odd"]


assert pset7.swap_ints([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]
assert pset7.swap_ints([2]) == [2]
assert pset7.swap_ints([1, 2]) == [2, 1]


assert pset7.group([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
assert pset7.group([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
assert pset7.group([1], 1) == [[1]]


assert pset7.sum_until([2, 4, 6, 8]) == [2, 6, 12, 20]
assert pset7.sum_until([2]) == [2]
assert pset7.sum_until([2, 4, 6]) == [2, 6, 12]


assert pset7.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

assert pset7.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

assert pset7.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
