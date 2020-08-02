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


FILE_SHORT = short()
COUNTER_DIFF = FILE_SHORT - 6
TOTAL_COUNTER = 0


def make_item_set():
    """
    Create list, create counter. Loop through following data, appending
    to list, until counter = 0. Enumerate to dictionary, omitting the
    item_counter. Return.
    """
    item_list = []
    item_counter = float()
    item_list.append(item_counter)
    item_counter = int(item_counter + 1)
    if item_counter > 0:
        for parameter in range(item_counter - 1):
            item_list.append(float())
    p_list = dict(enumerate(item_list[1:], 1))
    return p_list


def read_file_data():
    global TOTAL_COUNTER
    global COUNTER_DIFF
    while TOTAL_COUNTER < COUNTER_DIFF:
        item_list = []
        file_list = []
        item_counter = float()
        item_list.append(item_counter)
        TOTAL_COUNTER -= item_counter
        item_counter = int(item_counter + 1)
        if item_counter > 0:
            for parameter in range(item_counter - 1):
                item_list.append(float())
        p_list = dict(enumerate(item_list[1:], 1))
        file_list.append(p_list)
        return file_list
