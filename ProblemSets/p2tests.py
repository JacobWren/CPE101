# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set I
# Term:         Winter 2020


import pset2

assert pset2.print_hello("Jake") == None

assert pset2.cube(2) == 8
assert pset2.cube(3) == 27
assert pset2.cube(4) == 64

assert pset2.do_math(2, 3) == 6.0
assert pset2.do_math(2, 5) == 8.0
assert pset2.do_math(4, 5) == 8.5

assert pset2.get_hypotenuse(1, 1) == 1.4142135623730951
assert pset2.get_hypotenuse(1, 3) == 3.1622776601683795
assert pset2.get_hypotenuse(4, 1) == 4.123105625617661

assert pset2.get_distance(1, 2, 3, 4) == 2.8284271247461903
assert pset2.get_distance(1, 2, 3, 9) == 7.280109889280518
assert pset2.get_distance(1, 5, 3, 4) == 2.23606797749979

assert pset2.get_perimeter(1, 2, 3, 4, 5, 6) == 11.313708498984761
assert pset2.get_perimeter(1, 2, 3, 4, 5, 9) == 16.275849680179242
assert pset2.get_perimeter(4, 2, 3, 4, 5, 6) == 9.187600727863641

assert pset2.round_to_hundredths(5.123) == 5.12
assert pset2.round_to_hundredths(.834) == 0.83
assert pset2.round_to_hundredths(9.923) == 9.92
