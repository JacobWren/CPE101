# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020


from typing import Any, List, Tuple


def sort_ints(ints: List[int], mode: str) -> List[int]:
    if mode == "bubble":
        start = 0
        for i in range(len(ints)):
            ints = bubble_pass(ints)
        return ints
            
    elif mode == "selection":
        start = 0
        for i in range(len(ints)):
            ints = selection_pass(ints, start)
            start = start + 1
        return ints
    elif mode == "insertion":
        start = 0
        for i in range(len(ints)):
            ints = insertion_pass(ints, start)
            start = start + 1
        return ints
       

def bubble_pass(ints: List[int]) -> List[int]:
    l = []
    if len(ints) == 1:
        return ints
    for i in range(len(ints) - 1):
        if i == 0:
            if ints[i] > ints[i + 1]:
                l.append(ints[i + 1])
                l.append(ints[i])
            else:
             l.append(ints[i])
             l.append(ints[i + 1])
        elif i != 0:
            if l[i] > ints[i + 1]:
                l.append(l[i])
                l[i] = ints[i + 1]
            else:
             l.append(ints[i + 1])           
    return l



def find_min(l):
    if len(l) == 1:
        return l[0]
    for i in range(len(l) - 1):
        if i == 0:
            if l[i] > l[i + 1]:
                mini = l[i + 1]
            else:
                mini = l[i]
        else:
            if mini > l[i + 1]:
                mini = l[i + 1]
            else:
                mini = mini
    return mini


def selection_pass(ints: List[int], start: int) -> List[int]:
    h = ints.copy()
    if len(h) == 1:
        return h
    if len(h) == 0:
        return h
    if start > len(ints):
        return ints
    for i in range(1):
        mini = find_min(h[start:])
        index = h.index(mini)
        if h[start] > mini:
            h[index] = h[start]
            h[start] = mini
        start = start + 1
    return h

'''           
def insertion_pass(ints: List[int], start: int) -> List[int]:
    l = [ints[0]]
    for i in range(len(ints) - 1):
        h = ints.copy()
        #find_min(h[0:start + 1])    
        for k in l:
            j = 0
            y = 0
            if h[i + 1] < k:
                l.insert(j, h[i + 1])
                y = 1
                break
            j = j + 1
        if y == 0:
            l.append(h[i + 1])
            
                
        #start = start + 1
'''

def insertion_pass(ints, start):
    if start > len(ints):
        return ints
    ints_2 = ints.copy()
    for i in range(start - 1, -1, -1):
        if ints_2[i + 1] < ints_2[i]:
            p = ints_2[i]
            ints_2[i] = ints_2[i + 1]
            ints_2[i + 1] = p
    return ints_2


def binary_search(ints, n):
    start = 0
    end = (len(ints) - 1)
    while True:
        find_mid = (start + end) // 2
        if ints[find_mid] == n:
            return find_mid
        if n > ints[find_mid]:
            start = find_mid + 1
        elif n < ints[find_mid]:
            end = find_mid - 1
        if find_mid >= (len(ints) - 1) or find_mid <= 0:
            return -1

            





























    



































