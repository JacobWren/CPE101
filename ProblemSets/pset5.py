# Name:         Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 5
# Term:         Winter 2020


def reverse_string(chars: str) -> str:
    l = ""
    for i in chars:
        l = i + l
    return(l)


def translate_string(chars: str, old: str, new: str) -> str:
    l = ""
    for i in chars:
        if i == old:
            l = l + new
        else:
            l = l + i   
    return(l) 


def rotate_chars(chars: str, n_pos: int) -> str:
    l = ""
    for i in chars:
        if i.islower():
            if n_pos + ord(i) > ord('z'):
                st = ord('a') + ((( (( (n_pos - 1) % 26) + 1 )
                                    + ord(i) ) % ord('z'))) - 1
                l = l + chr(st)
            else:
                l = l + chr(ord(i) + n_pos)
        elif i.isupper():
            if n_pos + ord(i) > ord('Z'):
                st = ord('A') + (((n_pos + ord(i) ) % ord('Z'))) - 1
                l = l + chr(st)
            else:
                l = l + chr(ord(i) + n_pos)
        else:
            l = l + i
    return l


def encode_ascii(chars: str) -> str:
    l = ""
    for i in chars:
        l = l + f"{ord(i):03}"
    return l


def parse_word(words: str, position: int) -> str:
    Num_words = words.count(' ') + 1
    j = 0
    if position > Num_words:
        return ""
    else:
        for i in words.split():
            if j == position:
                return i
            j = j + 1


def swap_chars(chars: str) -> str:
    word = ""
    for i in range(1, len(chars), 2):
            word = word + chars[i] + chars[i - 1]
    if len(chars) % 2 == 0:
        return word
    else:
        word = word + chars[-1]
        return word
        

def is_palindrome(word: str) -> bool:
    end = (len(word) // 2) + 1
    tot = 0
    for i in range(0, end, 1):
        if word[i] == word[-1 - i]:
            tot = tot + 1
    return tot > 0


def decode_ascii(chars: str) -> str:
    l = ""
    start = 0
    end = 3
    save_prime = ""
    sum = ""
    for j in range(0, int( len(chars) / 3), 1):
        for i in range(start, end, 1):
            sum = sum + chars[i]
            if chars[i] != "0" or i % 2 == 0: 
                l = l + chars[i]
        if sum == "000":
            save = chr(0)
        else:
            save = chr(int(l) )
        save_prime = save_prime + save 
        start = start + 3
        end = end + 3
        sum = ""
        l = ""
    return save_prime
    

def make_substring(chars: str, start: int, stop: int, step: int) -> str:
    l = ""
    for i in range(start, stop, step):
        if i >= len(chars):
            break
        l = l + chars[i]
    return l


def longest_substring(s1: str, s2: str) -> str:
    save_prime_dub = ""
    champ = ""
    save_prime = ""
    for j in range(0, len(s1) ): 
        for k in range(0, len(s1) ): 
            save = make_substring(s1, j, k + 1, 1)
            if save in s2:
                save_prime = save
        if len(save_prime) > len(champ):
            champ = save_prime
        save_prime_dub = save_prime
    return champ
    

def transpose_string(chars: str, width: int) -> str:
    n = int( len(chars) / width)
    t = 0
    L = ""
    fin = ""
    for i in range(width):
        for j in range(t, len(chars), width):
            L = L + chars[j]
        fin = fin + L
        L = ""
        t = t + 1
    return fin
