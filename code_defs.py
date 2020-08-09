from item_sets import *


x = read_file_data()


class Item:

    def __init__(self, code, stave_no, p3, *args, **kwargs):
        self.code = code
        self.stave_no = stave_no
        self.p3 = p3

class Notes(Item):
    
    def __init__(self, code, stave_no, p3, *args, **kwargs):
        super().__init__(code, stave_no, p3)

    @classmethod
    def from_list(cls, p_list):
        pass

