"""
implementation for custom strings
"""

import random


class StringCustom(object):
    """class for custom string operation"""

    def __init__(self):
        """initialization"""

        self.value_list = []
        self.offset = 0
        self.length = 0
        self.hash = 0

    def __str__(self):
        """to string"""

        return "".join(self.value_list[self.offset: self.offset + self.length])

    def __getitem__(self, index):
        """get indexed value in position"""

        return self.char_at(index)

    @classmethod
    def from_str(cls, input_str):
        """create object from string"""

        str_c = cls()
        str_c.offset = 0
        str_c.value_list = [x for x in input_str]
        str_c.length = len(str_c.value_list)

        return str_c

    @classmethod
    def factory(cls, offset, length, value_list):
        """create object"""

        str_c = cls()
        str_c.offset = offset
        str_c.length = length
        str_c.value_list = value_list

        return str_c

    @classmethod
    def random_gen(cls, max_len, str_count):
        """generate custom string randomly"""

        str_list = []

        # random gen
        for _ in xrange(str_count):
            curr_str = []
            for _ in xrange(int(random.random() * max_len)):
                curr_char = chr(int(random.random() * 26) + 97)
                curr_str.append(curr_char)

            if curr_str:
                str_list.append("".join(curr_str))

        return [cls.from_str(x) for x in str_list]

    def length(self):
        """get length"""

        return self.length

    def char_at(self, index):
        """return char at indexed position"""

        if index < self.length:
            return self.value_list[index + self.offset]
        else:
            return None

    def substring(self, idx_from, idx_to):
        """get substring between index from/to"""
    
        assert (idx_to - idx_from + 1) <= self.length

        return self.__class__.factory(
            self.offset + idx_from,
            idx_to - idx_from + 1,
            self.value_list
        )

    def append(self, str_obj):
        """concatnation strings"""

    def suffixes(self):
        """compute suffixes"""

        str_list = []

        for idx in xrange(self.length):
            str_list.append(
                self.substring(idx, self.length - 1)
            )

        return str_list

    def lcp(self, str_obj):
        """compute longest common prefix"""

        str_len = min(self.length, str_obj.length)

        for idx in xrange(str_len):
            if self[idx] != str_obj[idx]:
                return idx

        return str_len

if __name__ == "__main__":

    sc = StringCustom.from_str("this is a book")

    for item in sc.suffixes():
        print item
