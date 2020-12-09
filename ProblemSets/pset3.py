# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 3
# Term:         Winter 2020


from typing import Union


def is_positive(x: int) -> bool:
    return x > 0



def both_positive(x: int, y: int) -> bool:
    return is_positive(x) and is_positive(y)


def is_triangle(a: int, b: int, c: int) -> bool:
    return (a + b > c) and (a + c > b) and (b + c > a)


def is_isosceles_triangle(a: int, b: int, c: int) -> bool:
    return is_triangle(a, b, c) and ( (a == b) or (a == c) or ( b == c) )


def is_int(n: Union[int, float]) -> bool:
    return float(n) == int(n) and len(str(n)) == len(str(int(n)))


def abs_val(n: int) -> int:
    return n if n >= 0 else -n


#def is_rotation(rotated: str, word: str) -> bool:
    #l = []
    #for i in range(len(word)):
        #l.append(word[-1] + word[0:-1])
        #word = l[i]
    #return rotated in l


def is_rotation(rotated: str, word: str) -> bool:
    return word in (rotated + rotated) and (len(rotated) == len(word))



# Branching
def max_of_two(x: int, y: int) -> int:
    if x >= y:
        return x
    else:
        return y


def max_of_three(x: int, y: int, z: int) -> int:
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z  


def mix_colors(a: str, b: str) -> str:
    if a == b:
        return a
    if (a == 'red' or a == 'yellow') and (b == 'yellow' or b == 'red'):
        return 'orange'
    elif (a == 'blue' or a == 'yellow') and (b == 'yellow' or b == 'blue'):
        return 'green'
    elif (a == 'red' or a == 'blue') and (b == 'blue' or b == 'red'):
        return 'purple'


def find_discriminant(a: int, b: int, c: int) -> Union[float, None]:
    disc = b ** 2 - (4 * a * c)
    if disc >= 0:
        return disc
    else:
        return None
    

def solve_poly(a: int, b: int, c: int) -> Union[float, None]:
    z = find_discriminant(a, b, c)
    if z == None:
        return None
    else:
       return ((z ** .5) - b) / (2 * a)
