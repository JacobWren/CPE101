# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 4
# Term:         Winter 2020


import pset4


assert pset4.mul(3, 4) == 12
assert pset4.mul(0, 2) == 0
assert pset4.mul(2, 0) == 0

assert pset4.exp(3, 0) == 1
assert pset4.exp(0, 2) == 0
assert pset4.exp(2, 3) == 8
assert pset4.exp(2, 1) == 2

assert pset4.div(3, 4) == 0
assert pset4.div(4, 2) == 2
assert pset4.div(81, 9) == 9
assert pset4.div(9, 9) == 1
assert pset4.div(9, 1) == 9

assert pset4.mod(15, 6) == 3
assert pset4.mod(2, 6) == 2
assert pset4.mod(18, 9) == 0
assert pset4.mod(9, 9) == 0

assert pset4.gcd(20, 10) == 10
assert pset4.gcd(5, 16) == 1
assert pset4.gcd(6, 15) == 3

assert pset4.is_prime(9) == False
assert pset4.is_prime(17) == True
assert pset4.is_prime(93) == False

assert pset4.is_prime(9) == False
assert pset4.is_prime(17) == True
assert pset4.is_prime(93) == False

assert pset4.sum_mul_table(5) == 225
assert pset4.sum_mul_table(4) == 100
assert pset4.sum_mul_table(3) == 36

assert pset4.sum_ints(2, 11, 3) == 15
assert pset4.sum_ints(2, 11, 4) == 18
assert pset4.sum_ints(1, 3, 1) == 3
assert pset4.sum_ints(2, 1, 1) == 0

assert pset4.rotate_string("computer", 5) == "putercom"
assert pset4.rotate_string("computer", 1) == "rcompute"
assert pset4.rotate_string("computer", 0) == "computer"

assert pset4.weave_strings("cmue", "optr") == "computer"
assert pset4.weave_strings("sine", "cec") == "science"
assert pset4.weave_strings("hg", "ih") == "high"
assert pset4.weave_strings("hg", "ihw") == "highw"

assert pset4.to_pig_latin("INTEGER") == "INTEGERYAY"
assert pset4.to_pig_latin("FLOAT") == "OATFLAY"
assert pset4.to_pig_latin("BY") == "BYAY"








