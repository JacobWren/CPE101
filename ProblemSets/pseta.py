# Name: Jacob Wren
# Course: CPE 101
# Instructor: Irene Humer
# Assignment: Problem set8
# Term: Winter 2020


from typing import Any, List, Tuple


def try_open(primary: str, secondary: str) -> List[str]:
    try:
        inf = open(primary, "r")
        return inf.readlines()
    except FileNotFoundError:
        try:
            inf = open(secondary, "r")
            return inf.readlines()
        except FileNotFoundError:
            return []


def count_zeros(ints: List[int]) -> int:
    counter = 0
    i = 0
    while True:
        try:
            1 / ints[i]
        except ZeroDivisionError:
            counter = counter + 1
        except IndexError:
            return counter
        i = i + 1
        

def try_isalnum(chars):
    j, q = 0, 0
    l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
     26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    while True:
        try:
            int(chars[q])
            q = q + 1
        except IndexError:
            return True
        except ValueError:
            while True:
                try:
                    int(chars[q], l[j])
                    break
                except IndexError:
                    return False
                except ValueError:
                    j = j + 1
            q, j = q + 1, 0


def get_numeric_type(number):
    try:
        n = str(number)
        int(n)
        return "int"
    except ValueError:
        return "float"


def get_sequence_type(sequence):
    try:
        sequence + []
        return "list"
    except TypeError:
        try:
            sequence + 'j'
            return "str"
        except TypeError:
            return "tuple"


def are_same_type(x, y):
    try:
        x + y
        return True
    except TypeError:
        return x is y
