# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020

import pset8

p1 = pset8.Point(1, 2)
p2 = pset8.Point(2, 4)
p3 = pset8.Point(1, 2)
p4 = pset8.Point(3, 4)
p5 = pset8.Point(1, -1)
p6 = pset8.Point(0, 0)
p7 = pset8.Point(4, 4)
p8 = pset8.Point(-6, 6)
p9 = pset8.Point(3, -10)
p10 = pset8.Point(4, -5)
p11 = pset8.Point(6, -2)
p12 = pset8.Point(-8, 2)
p13 = pset8.Point(6, 7)
p14 = pset8.Point(4, 5)
p15 = pset8.Point(-6, -2)
p16 = pset8.Point(1, -9)



assert p1 != p2
assert p1 == p3
assert p1 != p4


assert str(p1) == "(1, 2)"
assert str(p2) == "(2, 4)"
assert str(p3) == "(1, 2)"


assert p1.distance(p3) == 0.0
assert p1.distance(p2) == 2.23606797749979
assert p1.distance(p4) == 2.8284271247461903


assert p4.get_slope_intercept(p3) == (1.0, 1.0)
assert p1.get_slope_intercept(p2) == (2.0, 0.0)
assert p1.get_slope_intercept(p4) == (1.0, 1.0)


L1 = pset8.Line(p1, p2)
L2 = pset8.Line(p1, p1)
L3 = pset8.Line(p2, p3)
L4 = pset8.Line(p3, p4)
L5 = pset8.Line(p5, p4)
L6 = pset8.Line(p5, p4)
L5 = pset8.Line(p5, p4)
L5 = pset8.Line(p5, p4)
L5 = pset8.Line(p5, p4)
line1 = pset8.Line(p14, p11)
line2 = pset8.Line(p12, p13)
line3 = pset8.Line(p14, p11)
line4 = pset8.Line(p15, p16)
p18 = pset8.Point(2, 2)
p19 = pset8.Point(12, 3)
line5 = pset8.Line(p18, p19)



p10 = pset8.Point(4, -5)
p11 = pset8.Point(6, -2)
p12 = pset8.Point(-8, 2)
p13 = pset8.Point(6, 7)
p14 = pset8.Point(4, 5)
p15 = pset8.Point(-6, -2)
p16 = pset8.Point(1, -9)
p17 = pset8.Point(0, 0)

assert L1 != L2
assert L1 == L3
assert L1 != L4


assert (str(L1)) == "y = 2.0x + 0.0"
assert (str(L2)) == 'y = 0.0x + 2.0'
assert (str(L5)) == "y = 2.5x - 3.5"




assert (str(L1.to_parallel(p1))) == 'y = 2.0x + 0.0'
assert (str(L2.to_parallel(p3))) == 'y = 0.0x + 2.0'
assert (str(L3.to_parallel(p5))) == 'y = 2.0x - 3.0'
assert (str(line5.to_parallel(p17))) == 'y = 0.1x + 0.0'



assert (str(L1.to_perpendicular())) == 'y = -0.5x + 0.0'
assert (str(L5.to_perpendicular())) == 'y = -0.4x - 3.5'
assert (str(L3.to_perpendicular())) == 'y = -0.5x + 0.0'




c1 = pset8.Circle(p1, 2)
c2 = pset8.Circle(p1, 2)
c3 = pset8.Circle(p2, 4)
c4 = pset8.Circle(p3, 4)
c5 = pset8.Circle(p4, 4)
c6 = pset8.Circle(p6, 1)


assert c1 == c2
assert c2 != c3
assert c3 != c4


assert str(c1) == "2r @ (1, 2)"
assert str(c2) == "2r @ (1, 2)"
assert str(c4) == "4r @ (1, 2)"


assert c1.overlaps(c1) == True
assert c2.overlaps(c3) == True
assert c3.overlaps(c4) == True


assert c1.bisects(L1) == True
assert c2.bisects(L2) == True
assert c3.bisects(L3) == True
assert c5.bisects(L3) == False

assert pset8.get_point_distances([p1, p2, p3]) == [2.23606797749979,
                                                   4.47213595499958,
                                                   2.23606797749979]
assert pset8.get_point_distances([p4]) == [5.0]
assert pset8.get_point_distances([p4, p5]) == [5.0, 1.4142135623730951]


assert pset8.get_circle_distances([c1, c2, c3]) == [2.23606797749979,
                                                    2.23606797749979,
                                                    4.47213595499958]
assert pset8.get_circle_distances([c4]) == [2.23606797749979]
assert pset8.get_circle_distances([c4, c5]) == [2.23606797749979, 5.0]


assert pset8.are_in_first_quadrant([p1, p2, p3]) == [p1, p2, p3]
assert pset8.are_in_first_quadrant([p4]) == [p4]
assert pset8.are_in_first_quadrant([p4, p5]) == [p4]


assert pset8.overlaps_unit_circle([c1, c2]) == [c1, c2]
assert pset8.overlaps_unit_circle([c3]) == [c3]
assert pset8.overlaps_unit_circle([c4, c5]) == [c4]



