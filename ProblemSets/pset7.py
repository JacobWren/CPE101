# Name: Jacob Wren
# Course: CPE 101
# Instructor: Daniel Kauffman
# Assignment: Problem set8
# Term: Winter 2020


from typing import Any, List, Tuple


def get_reciprocals(ints: List[int]) -> List[float]:
    #return [1 / i for i in ints]
    return [1 / i for i in ints if i != 0]     


def get_parities(ints: List[int]) -> List[str]:
    return ["even" if i % 2 == 0 else "odd" for i in ints]


#def swap_ints(ints: List[int]) -> List[int]:
#    for i in range(0, len(ints) - 1, 2):
#        temp = ints[i]
 #       ints[i] = ints[i + 1]
  #      ints[i + 1] = temp
  #  return ints

        
def swap_ints(ints):
    #return [ints[i + 1] for i in range(0, len(ints) - 1,2)]
    #return [ints[i] for i in range(0, len(ints), 2) if i % 2 == 0]
    #return [ints[i] if i % 2 != 0 else ints[i] for i in range(0, len(ints))] 
    #return [ints[i + 1] if i % 2 == 0 else ints[i - 1] for i in range(0, len(ints) - 1)]
    if len(ints) % 2 != 0:
        return [ints[i - 1] if i % 2 != 0 else ints[i + 1] for i in range(0,
                                 len(ints) - 1)] + [ints[len(ints) - 1]]
    else:
        return [ints[i - 1] if i % 2 != 0 else ints[i + 1] for i in range(0,
                                 len(ints))]
    #return [ints[i - 1] if i % 2 != 0 else ints[i + 1] if i == (len(ints) - 1) else ints[len(ints) - 1] for i in range(0, len(ints) - 1)]
    #return [ints[len(ints) - 1] if (i == (len(ints) - 1) and i % 2 != 0) else ints[i - 1] if i % 2 != 0 else ints[i + 1] for i in range(0, len(ints))]


def group(ints: List[int], size: int) -> List[List[int]]:
    #return [[ints[i] for j in range(size)] for i in range(size)]
    #return [[ints[i] for j in range(size)] for i in range(0, size, size)]
    return [ints[i:i + size] for i in range(0, len(ints), size)]


def sum_until(ints: List[int]) -> List[int]:
    return [ sum(ints[0:i]) for i in range(1, len(ints) + 1) ]
                
    







def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [ [j[i] for j in i] for i in range(len(matrix[0]))]


























