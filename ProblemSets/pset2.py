# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 2
# Term:         Winter 2020


def print_hello(name: str) -> None:                                 
    print("Hello " + name)

    
def get_numbers() -> int:
    num1 = int(input("Enter an integer: "))
    num2 = int(input("Enter an integer: "))
    return num1 + num2


def cube(x: int) -> int:
    return x ** 3


def do_math(x: int, y: int) -> float:
    return ((3 * (x ** 2)) + (4 * y)) / (2 * x)


def get_hypotenuse(a: int, b: int) -> float:
    return (((a ** 2) + (b ** 2)) ** .5)


def get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return get_hypotenuse(x2 - x1, y2 - y1)

    
def get_perimeter(x1: int, y1: int, x2: int, y2: int,
                  x3: int, y3: int) -> float:
    one = get_distance(x1, y1, x2, y2)
    two = get_distance(x1, y1, x3, y3)
    three = get_distance(x2, y2, x3, y3)
    return one + two + three


def round_to_hundredths(x: float) -> float:
    first = (((x * 10000000) / 1000000) // 1) % 10
    last = (((x * 10000000) / 100000) // 1) % 10
    third = (((x * 10000000) / 10000) // 1) % 10
    one = (x * 100) // 100
    a = (last * 10) + (first * 100) 
    w = one + (a / 1000)
    nep = w + (((third * 2) // 10) / 100)
    return nep
