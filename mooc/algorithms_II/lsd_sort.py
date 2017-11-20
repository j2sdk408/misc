"""
implementation for least-signficant-digit-first string sort
"""

from str_custom import StringCustom

class LsdSort(object):
    """class for LSD string sort"""

    def __init__(self, str_list):
        """initialization"""

        self.str_list = str_list
        self.sort()

    def __str__(self):
        """to string"""

        return "\n".join([str(x) for x in self.str_list])

    def sort(self):
        """sort string"""

        # extra space for re-ordering
        reorder_list = [None] * len(self.str_list)

        # starts from the longest position
        max_len = max([x.length for x in self.str_list])

        def map_idx(x):
            """calculate map index including None"""
            if x is None:
                return 0
            else:
                return ord(x) + 1

        # sort from right to left
        for char_idx in xrange(max_len - 1, -1, -1):

            # ascii map + None@1 + extra space@0
            key_map = [0] * (128 + 1 + 1)

            # count frequency
            for idx in xrange(len(self.str_list)):
                curr_char = self.str_list[idx][char_idx]
                key_map[map_idx(curr_char) + 1] += 1

            # culmulate map
            for idx in xrange(1, len(key_map)):
                key_map[idx] += key_map[idx - 1]

            # sort by copying to reorder list
            for idx in xrange(len(self.str_list)):
                curr_char = self.str_list[idx][char_idx]
                curr_map_idx = map_idx(curr_char)

                curr_key = key_map[curr_map_idx]
                key_map[curr_map_idx] += 1

                reorder_list[curr_key] = self.str_list[idx]

            # copy back
            for idx, item in enumerate(reorder_list):
                self.str_list[idx] = item


if __name__ == "__main__":

    import random

    max_len = 20
    str_count = 30
    str_list = []

    # random gen
    for _ in xrange(str_count):
        curr_str = []
        for _ in xrange(int(random.random() * max_len)):
            curr_char = chr(int(random.random() * 25) + 97)
            curr_str.append(curr_char)

        str_list.append("".join(curr_str))

    sc_list = [StringCustom.from_str(x) for x in str_list]
    lsd = LsdSort(sc_list)

    print lsd

