from item_sets import *


x = read_file_data()


class Parameters:

    def __init__(self, code, p2, p3, p4, *args):
        self.code = code
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    @classmethod
    def from_list(cls, p_list):
        pass

