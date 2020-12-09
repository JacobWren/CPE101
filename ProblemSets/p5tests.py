# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   Problem Set 4
# Term:         Winter 2020



import pset5

assert pset5.reverse_string("chars") == "srahc"
assert pset5.reverse_string("Harshit") == "tihsraH"
assert pset5.reverse_string("c") == "c"


assert pset5.translate_string("I LOVE 101", "O", "I") == "I LIVE 101"
assert pset5.translate_string("Jacop", "p", "b") == "Jacob"
assert pset5.translate_string("Jakm", "m", "e") == 'Jake'


assert pset5.rotate_chars('w', 6) == 'c'
assert pset5.rotate_chars('wx', 6) == 'cd'
assert pset5.rotate_chars('9', 6) == '9'
assert pset5.rotate_chars('!w', 6) == '!c'
assert pset5.rotate_chars('A', 1) == 'B'
assert pset5.rotate_chars('Z', 1) == 'A'


assert pset5.encode_ascii("ABC") == '065066067'
assert pset5.encode_ascii("~~~") == '126126126'
assert pset5.encode_ascii("") == ''
assert pset5.encode_ascii(" ") == '032'


assert pset5.parse_word("jake wren is cool", 0) == 'jake'
assert pset5.parse_word("jake wren is cool", 1) == 'wren'
assert pset5.parse_word("jake wren is cool", 9) == ''


assert pset5.swap_chars("AaBbCcD") == "aAbBcCD"
assert pset5.swap_chars("AaBbCc") == 'aAbBcC'
assert pset5.swap_chars("") == ''


assert pset5.is_palindrome("racecar") == True
assert pset5.is_palindrome("acecar") == False
assert pset5.is_palindrome("tacocat") == True


assert pset5.is_palindrome("racecar") == True
assert pset5.is_palindrome("acecar") == False
assert pset5.is_palindrome("tacocat") == True


assert pset5.decode_ascii("065066067") == 'ABC'
assert pset5.decode_ascii("122066067") == 'zBC'
assert pset5.decode_ascii("") == ''
assert pset5.decode_ascii("000") == '\x00'
assert pset5.decode_ascii("000065") == '\x00A'



assert pset5.make_substring("COMPUTER", 0, 10, 3) == 'CPE'
assert pset5.make_substring("Jpapkpep", 0, 7, 2) == 'Jake'
assert pset5.make_substring("", 0, 7, 2) == ''


assert pset5.longest_substring("rapjake", "rapojake") == 'jake'
assert pset5.longest_substring("abcddf", "pqrddk") == 'dd'
assert pset5.longest_substring("", "") == ''


assert pset5.transpose_string("ABCDEFGHI", 3) == 'ADGBEHCFI'
assert pset5.transpose_string("ABCDEFGHIJKL", 3) == 'ADGJBEHKCFIL'
assert pset5.transpose_string("", 3) == ''














