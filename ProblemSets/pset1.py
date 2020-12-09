# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set I
# Term:         Winter 2020


def problem_1() -> None:
    x = int(input("Enter a number from 1 to 20: "))
    (((x*2) + 10) /2) - x
    print(x)

    
def problem_2() -> None:
    y = int(input("Enter a number: "))
    z = int(input("Enter a number: "))
    a = y + z
    b = a + z
    c = b + a
    d = c + b
    e = d + c
    f = e + d
    g = f + e
    h = g + f
    print((y + z + a + b + c + d + e + f + g + h)/e)


def problem_3() -> None:
    x = int(input("Enter a 4 digit number with unique integers: "))
    last = x % 10
    first = (x - (x % 100)) // 1000
    small = min(last,first)
    big = max(last,first)
    sub = big - small
    tot = ((sub % 10) + ((sub - (sub % 10) ) // 10))
    print(tot)
    

def problem_4() -> None:
    x = int(input("Enter a number from 1 to 50 not divisible by 7: "))
    y = x / 7
    one = (((y * 1000000)/100000)//1) % 10
    two = (((y * 1000000)/10000)//1) % 10
    three = (((y * 1000000)/10000)//1) % 10
    four = (((y * 1000000)/10000)//1) % 10
    five = (((y * 1000000)/10000)//1) % 10
    six = (((y * 1000000)/10000)//1) % 10
    tot = one + two + three + four + five + six
    print(tot)


if __name__ == "__main__":
    problem_1()
    problem_2()
    problem_3()
    problem_4()
