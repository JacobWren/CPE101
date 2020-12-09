# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 3
# Term:         Winter 2020

import pset3

assert pset3.is_positive(2) == True
assert pset3.is_positive(0) == False
assert pset3.is_positive(4) == True

assert pset3.both_positive(1, 2) == True
assert pset3.both_positive(1, 0) == False
assert pset3.both_positive(1, 99) == True

assert pset3.is_triangle(1, 2, 3) == False
assert pset3.is_triangle(1, 2, 4) == False
assert pset3.is_triangle(3, 2, 3) == True

assert pset3.is_isosceles_triangle(1, 3, 2) == False
assert pset3.is_isosceles_triangle(1, 2, 4) == False
assert pset3.is_isosceles_triangle(1, 2, 2) == True

assert pset3.is_int(.3) == False
assert pset3.is_int(3.2) == False
assert pset3.is_int(2) == True

assert pset3.abs_val(1) == 1
assert pset3.abs_val(-1) == 1
assert pset3.abs_val(0) == 0

assert pset3.is_rotation('ordw', 'word') == True
assert pset3.is_rotation('dwro', 'word') == False
assert pset3.is_rotation('dwor', 'word') == True

assert pset3.max_of_two(2, 5) == 5
assert pset3.max_of_two(5, 5) == 5
assert pset3.max_of_two(6, 5) == 6

assert pset3.max_of_three(2, 7, 4) == 7
assert pset3.max_of_three(9, 0, 10) == 10
assert pset3.max_of_three(9, 3, 9) == 9

assert pset3.mix_colors('red', 'yellow') == 'orange'
assert pset3.mix_colors('yellow', 'blue') == 'green'
assert pset3.mix_colors('red', 'blue') == 'purple'
assert pset3.mix_colors('red', 'red') == 'red'

assert pset3.find_discriminant(1, 2, 3) == None
assert pset3.find_discriminant(1, 16, 3) == 244
assert pset3.find_discriminant(2, 6, 4) == 4

assert pset3.solve_poly(1, 2, 3) == None
assert pset3.solve_poly(1, 16, 3) == -0.18975032409334602
assert pset3.solve_poly(1, 4, 3) == -1.0
