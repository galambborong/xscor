from struct import *


FILENAME = "PYTHON.MUS"
f = open(FILENAME, "rb")

# Trailing commas prevent the value being returned as a tuple.


def short():
    """
    Read short, unpack, return.

    C type: short
    Python type: integer
    Standard size: 2 bytes

    See https://docs.python.org/3/library/struct.html#format-characters for more info
    """
    short, = unpack("h", f.read(2))
    return short


def float():
    """
    Read float, unpack, return.

    C type: float
    Python type: float
    Standard size: 4 bytes

    See https://docs.python.org/3/library/struct.html#format-characters for more info
    """
    float, = unpack("f",f.read(4))
    return float

TOTAL_COUNTER = short()
ITEM_NUMBER = 0


def make_item_set():
    """
    Create list, create counter. Loop through following data, appending
    to list, until counter = 0. Print list to screen.
    """
    item_list = []
    item_counter = float()
#    TOTAL_COUNTER -= 1
    item_list.append(item_counter)
    item_counter = int(item_counter + 1)
    if item_counter > 0:
        for parameter in range(item_counter - 1):
            item_list.append(float())
#            TOTAL_COUNTER -= 1
    return(item_list)


def assign_item_set():
    if TOTAL_COUNTER > 0:
        ITEM_NUMBER += 1
        number = str(ITEM_NUMBER)
#        item_"number" = make_item_set()

    
