# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020


import psetb


assert psetb.parse_term("Fall '20") == "Fall '20"
assert psetb.parse_term("Spring '20") == "Spring '20"
assert psetb.parse_term("Winter '20") == "Winter '20"



assert psetb.parse_time("12:01:59PM") == '12:01:59PM'
assert psetb.parse_time("12:01:59") == '12:01:59'
assert psetb.parse_time("1:01:59PM") == '01:59PM'
