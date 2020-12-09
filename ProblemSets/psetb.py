# Name: Jacob Wren
# Course: CPE 101
# Instructor: Irene Humer
# Assignment: Problem setb
# Term: Winter 2020


import re


def parse_term(text):
    hold = re.search(r"(Winter|Spring|Fall|Summer) (([0-9]{4})|('[0-9]{2}))", text)
    return hold.group()


def parse_time(text):
    hold = re.search(r"([0-1][0-9]:[0-5][0-9](:[0-5][0-9])?(AM|PM)?)", text)
    return hold.group()
