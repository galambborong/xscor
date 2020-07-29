from struct import *

FILENAME = "PYTHON.MUS"
f = open(FILENAME, "rb")


def short():
    short, = unpack("h", f.read(2))
    return short

def float():
    float, = unpack("f",f.read(4))
    return float


# ITEM_NUMBER = 1


def make_item_set():
    p_list = []
#    ITEM_COUNTER, = float() THIS DOESN'T WORK YOU FOOL
    p_list.append(float())
    ITEM_COUNTER = int(p_list[0] + 1)
    if ITEM_COUNTER > 0:
        for p in range(ITEM_COUNTER - 1):
#            p_number, = float()
            p_list.append(float())
    print(p_list)


