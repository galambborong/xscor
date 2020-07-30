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
    (short,) = unpack("h", f.read(2))
    return short


def float():
    """
    Read float, unpack, return.

    C type: float
    Python type: float
    Standard size: 4 bytes

    See https://docs.python.org/3/library/struct.html#format-characters for more info
    """
    (float,) = unpack("f", f.read(4))
    return float


TOTAL_COUNTER = short()


def make_item_set():
    """
    Create list, create counter. Loop through following data, appending
    to list, until counter = 0. Enumerate, convert to dictionary whilst 
    omitting the item_counter, return.
    """
    item_list = []
    item_counter = float()
    item_list.append(item_counter)
    item_counter = int(item_counter + 1)
    if item_counter > 0:
        for parameter in range(item_counter - 1):
            item_list.append(float())
    item_set = list(enumerate(item_list))
    x = item_set[1:-1]
    p_list = dict(x)
    return p_list
