from item_sets import *

"""
This is purely for shortlisting things in
my working. 
"""

x = read_file_data()


def notes(x):
    for item in x:
        if item[1] == 1.0:
            print(item)


def rests(x):
    for item in x:
        if item[1] == 2.0:
            print(item)


def clefs(x):
    for item in x:
        if item[1] == 3.0:
            print(item)


def lines(x):
    for item in x:
        if item[1] == 4.0:
            print(item)


def slurs(x):
    for item in x:
        if item[1] == 5.0:
            print(item)


def beams(x):
    for item in x:
        if item[1] == 6.0:
            print(item)


def sys_lines(x):
    for item in x:
        if item[1] == 7.0:
            print(item)


def staves(x):
    for item in x:
        if item[1] == 8:
            print(item)


def symbol_lib(x):
    for item in x:
        if item[1] == 9:
            print(item)


def numbers(x):
    for item in x:
        if item[1] == 10:
            print(item)


def barlines(x):
    for item in x:
        if item[1] == 14:
            print(item)


def text(x):
    for item in x:
        if item[1] == 16:
            print(item)


def key_sig(x):
    for item in x:
        if item[1] == 17:
            print(item)


def time_sig(x):
    for item in x:
        if item[1] == 18:
            print(item)
