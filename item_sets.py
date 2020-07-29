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


# ITEM_NUMBER = 1


def make_item_set():
    """
    Create list, create counter. Loop through following data, appending
    to list, until counter = 0. Print list to screen.
    """
    p_list = []
#    ITEM_COUNTER, = float() THIS DOESN'T WORK YOU FOOL
    p_list.append(float())
    ITEM_COUNTER = int(p_list[0] + 1)
    if ITEM_COUNTER > 0:
        for p in range(ITEM_COUNTER - 1):
#            p_number, = float()
            p_list.append(float())
    print(p_list)


