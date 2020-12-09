# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 4
# Term:         Winter 2020


def all_input() -> str:
    b = 'a'
    c = ''
    while b != 0:
        a = input("Enter: ")
        b = len(a)
        c = c + a
    return c


def mul(x: int, y: int) -> int:
    n = max(x, y)
    m = min(x, y)
    z = 0
    j = 0
    while j < n:
        z = z + m
        j = j + 1
    return z


def exp(x: int, y: int) -> int:
    if y == 0:
        return 1
    elif y == 1:
        return x
    sum = 0
    tot = x
    if y == 2:
        num_times = 1
        while num_times < y:
            sum = mul(x, x) + sum
            num_times = num_times + 1
        return sum
    else:
        num_times = 1
        while num_times < y:
            tot = mul(tot, x)
            num_times = num_times + 1
        return tot


def div(x: int, y: int) -> int:
    numerator = x
    s = 0
    if  y > x:
        return 0
    elif y == x:
        return 1
    elif y == 1:
        return x
    else:
        while numerator >= y:
            numerator = numerator - y
            s = s + 1
        return s
    

def mod(x: int, y: int) -> int:
    numerator = x
    if  y > x:
        return x
    elif y == x:
        return 0
    else:
        while numerator >= y:
            numerator = numerator - y
        return numerator    


def gcd(x: int, y: int) -> int:
    d = min(x, y)
    i = 1
    while i <= d:
        if x % i == 0 and y % i == 0:
            gcd = i
        i = i + 1
    return gcd


def is_prime(x: int) -> bool:
    i = 2
    tot = 0
    while i < x:
        if x % i == 0:
            tot = tot + 1
        i = i + 1
    return tot == 0    


def sum_ints(start: int, stop: int, step: int) -> int:
    if stop <= start:
        return 0
    sum = start - step
    tot = 0
    while start < stop:
        sum = sum + step
        tot = tot + sum
        start = start + step
    return tot


def sum_mul_table(max_int: int) -> int:
    j = 1
    i = 1
    sum = 0
    while j <= max_int:
        k = (max_int * i) + 1
        tot = sum_ints(j, k, i)
        sum = sum + tot
        j = j + 1
        i = i + 1
    return sum


def rotate_string(chars: str, n_rot: int) -> str:
    i = 0
    while i < n_rot:
        length = len(chars) - 1
        chars = chars[length] + chars[0:length]
        i = i + 1
    return chars


def weave_strings(s1: str, s2: str) -> str:
    min_len = min(len(s1), len(s2))
    i = 0
    word_prime = ''
    while i < min_len:
        word  = s1[i] + s2[i]
        word_prime = word_prime + word
        i = i + 1
    if len(s1) == len(s2):
        return word_prime
    else:
        if len(s1) > len(s2):
            end = s1
        else:
            end = s2
        left = max(len(s1), len(s2)) - min_len
        return word_prime + end[-left:]


def to_pig_latin(word: str) -> str:
    if(word[0] == 'A' or word[0] == 'E' or word[0] == 'I'
       or word[0] == 'O' or word[0] == 'U'):
        return word + 'YAY'
    else:
        i = 0
        length = len(word) 
        while(word[0] != 'A' and word[0] != 'E' and word[0] != 'I'
       and word[0] != 'O' and word[0] != 'U'): 
            word = word[1:length] + word[0]
            i = i + 1
            if i >= length:
                break
        return word + 'AY'
