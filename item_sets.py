from struct import *

FILENAME = "PYTHON.MUS"
f = open(FILENAME, "rb")


def file_counter():
    (COUNTER,) = unpack("h", f.read(2))
    return COUNTER


ITEM_NUMBER = 1
p_list = []


def item_set():
    (ITEM_COUNTER,) = unpack("f", f.read(4))
    return ITEM_COUNTER
    p_list.append(ITEM_COUNTER)
    if ITEM_COUNTER > 0:
        (p_number,) = unpack("f", f.read(4))
        p_list.append(p_number)
        ITEM_COUNTER -= 1
        return p_number
    else:
        ITEM_NUMBER += 1
        return item_set
