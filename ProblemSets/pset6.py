# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Pset6
# Term:         Winter 2020


from typing import Any, List, Tuple


def poly_add(poly1: List[int], poly2: List[int]) -> List[int]:
    sum = []
    diff = abs(len(poly1) - len(poly2))
    if len(poly1) < len(poly2):
        smallest = poly1.copy()
        j = 1
    else:
        smallest = poly2.copy()
        j = 0
    if diff != 0:
        for i in range(0, diff):
            smallest.append(0)      
    for i in range(0, len(smallest) ):
        if j == 1:
            sum.append(smallest[i] + poly2[i])
        else:
            sum.append(poly1[i] + smallest[i])
    return sum


def poly_mul(poly1: List[int], poly2: List[int]) -> List[int]:
    mul = []
    if poly1 == [0] or poly2 == [0]:
        return [0]
    for j in range(0, len(poly1) ):
        for i in range(0, len(poly2) ):
            mul.append(poly1[j] * poly2[i])
        for k in range(0, j):
            mul.insert(0, 0)
        hold = mul.copy()
        if j != 0:
            hold_latter = poly_add(hold_latter, hold)
        if j != 0:
            hold_latter = hold_latter 
        else:
            hold_latter = hold.copy()
        mul = []
    return hold_latter


def get_mode(ints: List[int]) -> int:
    for i in range(len(ints) - 1, -1, -1):
        most = ints.count(ints[i])
        if i != len(ints) - 1:
            if most > most_latter:
                most_latter = most
            else:
                most_latter = most_latter
        else:
            most_latter = most
        if i == len(ints) - 1:
            mode = ints[i]
        else:
            if most >= most_latter:
                mode = ints[i]
            else:
                mode = mode
    return mode


def index_of_smallest(ints: List[int]) -> int:
    if len(ints) == 0:
        return -1
    else:
        for i in range(len(ints) - 1, -1, -1):
            most = ints[i]
            if i == len(ints) - 1:
                index = i
            if i != len(ints) - 1:
                if most <= mode:
                    index = i
                else:
                    index = index
            if i == len(ints) - 1:    
                mode = most
            else:
                if most <= mode:
                    mode = most
        return index


def has_duplicates(ints: List[int]) -> bool:
    if len(ints) == 0:
        return False
    else:
        for i in range(0, len(ints) ):
            if ints[i] != 0:
                if ints.count(ints[i]) > 1:
                    return True
        return False


def products(int_lists: List[List[int]]) -> List[int]:
    prod_list = []
    for i in int_lists:
        if len(i) == 0:
            prod_list.append(0)
        else:
            mult = 1
            for j in i:
                mult = mult * j
            prod_list.append(mult)
    return prod_list


def fibonacci(n: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]    
    l = [0, 1]
    for i in range(2, n):
        l = l
        l.append(l[i-1] + l[i-2])
    return l
        

def geo_mean(floats: List[float]) -> float:
    if len(floats) == 0:
        return 0
    mult = 1
    N = len(floats)
    for j in floats:
        mult = mult * j
    return mult ** (1 / N)


def harmonic_mean(floats: List[float]) -> float:
    recip_sum = 0
    num_negs = 0
    if len(floats) == 0:
        return 0
    if floats == [0]:
        return 0
    for i in floats:
        if i > 0:
            recip_sum = recip_sum + (1 / i)
        else:
            num_negs = num_negs + 1
    return (len(floats) - num_negs) / recip_sum 


def nest_lists(n: int) -> List[Any]:
    x = []
    for i in range(n - 1):
        x = [x]
    return x


def solve_bool_exp(bool_exp: List[str], bools:
                   Tuple[bool, bool]) -> bool:
    if bool_exp[0] == "not":
        x, operator = not bools[0], bool_exp[2]
        if bool_exp[3] == "not":
            y = not bools[1]
        else:
            y = bools[1]
        if bool_exp[2] == "and":
            return x and y
        return x or y
    else: 
        x, operator = bools[0], bool_exp[1]
        if bool_exp[2] == "not":
            y = not bools[1]
        else:
            y = bools[1]
        if bool_exp[1] == "and":
            return x and y
        return x or y
