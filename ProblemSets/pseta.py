# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
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
        
'''            
def empty_list(chars):
    q = 0
    try:
        chars[q]
    except IndexError:
        return False
'''

def try_isalnum(chars):
    j, q = 0, 0
    l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
     26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    while True:
        try:
            int(chars[q])
            #break
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
    #return True


'''
def try_isalnum(chars):
    j, q = 0, 0
    l = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
     26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
   # try:
       # chars[q]
   # except IndexError:
    #    return False
    while True:
        try:
            int(chars[q])
            break
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
    return True
'''

'''      
def get_numeric_type(number):
    try:
        num = number - (number // 1)
        1 / num
        return "float"
    except ZeroDivisionError:
        return "int"
'''

'''
def get_numeric_type(number):
    try:
        return type(number) is int
    except ZeroDivisionError:
        return "int"
'''


def get_numeric_type(number):
    try:
        n = str(number)
        int(n)
        return "int"
    except ValueError:
        return "float"



def get_sequence_type(sequence):
    try:
        #sequence[0] = 1
        sequence + []
        return "list"
    except TypeError:
        try:
            sequence + 'j'
            return "str"
        except TypeError:
            return "tuple"



def are_same_type(x, y):
    #try:
        #x in [None] and y in [None]
        #return True
    try:
        x + y
        return True
    except TypeError:
        return x is y
        #return False
    
# (NoneType, string, list, or tuple)

    
    
































    
    









    




















