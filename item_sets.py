from struct import *


"""
    For information on struct and binary data types, see
    https://docs.python.org/3/library/struct.html#format-characters

    Types used:

    C type: short, Python: integer, 2 bytes
    C type: float, Python: float, 4 bytes

"""


FILENAME = "PYTHON.MUS"
f = open(FILENAME, "rb")

# Trailing commas prevent the value being returned as a tuple.


def short():
    (short,) = unpack("h", f.read(2))
    return short


def float():
    (float,) = unpack("f", f.read(4))
    return float


FILE_SHORT = short()
COUNTER_DIFF = FILE_SHORT - 6
total_counter = 0


def make_item_set():
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
    file_list = []
    global total_counter
    global COUNTER_DIFF
    while total_counter < COUNTER_DIFF:
        x = make_item_set()
        file_list.append(x)
        total_counter += len(x) + 1
    return file_list
