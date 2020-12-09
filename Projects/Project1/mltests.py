# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Moonlander Project
# Term:         Winter 2020

import moonlander

assert moonlander.update_fuel(100, 5) == 95
assert moonlander.update_fuel(100, 4) == 96
assert moonlander.update_fuel(-1, 5) == 0

assert moonlander.update_acceleration(1.62, 5) == 0
assert moonlander.update_acceleration(1.62, 10) == 1.62
assert moonlander.update_acceleration(1.62, 4) == -0.32399999999999995

assert moonlander.update_velocity(0, 5) == 5
assert moonlander.update_velocity(10, 10) == 20
assert moonlander.update_velocity(0, 0) == 0

assert moonlander.update_altitude(-2, 0, 0) == 0
assert moonlander.update_altitude(103, 0, 2) == 104.0
assert moonlander.update_altitude(103, 19, 2) == 123.0
