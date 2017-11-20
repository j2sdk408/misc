"""
implementation for least-signficant-digit-first string sort
"""

from str_custom import StringCustom

class MsdSort(object):
    """class for MSD string sort"""

    def __init__(self, str_list):
        """initialization"""

        self.str_list = str_list
        self._aux_list = [None] * len(self.str_list)

        self.sort(0, len(self.str_list) - 1, 0)

    def __str__(self):
        """to string"""

        return "\n".join([str(x) for x in self.str_list])

    @staticmethod
    def map_idx(x):
        """calculate map index including None"""

        if x is None:
            return 0
        else:
            return ord(x) + 1

    def sort(self, idx_st, idx_end, char_idx):
        """sort string"""

        # terminate whtn index overlap
        if idx_st >= idx_end:
            return

        # ascii map + None@1 + extra space@0
        key_map = [0] * (128 + 1 + 1)
        key_map2 = [0] * (128 + 1 + 1)

        # count frequency
        char_found = False
        for idx in xrange(idx_st, idx_end + 1):
            curr_char = self.str_list[idx][char_idx]

            if curr_char is not None:
                char_found = True

            key_map[self.map_idx(curr_char) + 1] += 1
            key_map2[self.map_idx(curr_char) + 1] += 1

        # terminate when no char to be found
        if not char_found:
            return

        # culmulate map
        for idx in xrange(1, len(key_map)):
            key_map[idx] += key_map[idx - 1]

        # sort by copying to reorder list
        for idx in xrange(idx_st, idx_end + 1):
            curr_char = self.str_list[idx][char_idx]
            curr_map_idx = self.map_idx(curr_char)

            curr_key = key_map[curr_map_idx]
            key_map[curr_map_idx] += 1

            self._aux_list[curr_key] = self.str_list[idx]

        # copy back
        for idx in xrange(idx_st, idx_end + 1):
            self.str_list[idx] = self._aux_list[idx - idx_st]

        # sort recursively toward right
        next_start = 0

        for count in key_map2:
            if count != 0:
                self.sort(
                    idx_st + next_start, 
                    idx_st + next_start + count - 1, 
                    char_idx + 1
                )
                next_start += count


if __name__ == "__main__":

    from lsd_sort import LsdSort

    sc_list = StringCustom.from_str(
        "itwasbestitwasw"
    ).suffixes()

    msd = MsdSort(sc_list)

    lrs = StringCustom.from_str("")

    for idx in xrange(len(sc_list) - 1):
        curr_len = msd.str_list[idx].lcp(msd.str_list[idx + 1])

        if curr_len > lrs.length:
            lrs = msd.str_list[idx].substring(0, curr_len - 1)

    print lrs
