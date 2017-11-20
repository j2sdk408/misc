"""
implementation for least-signficant-digit-first string sort
"""

from str_custom import StringCustom

class Quick3Sort(object):
    """class for 3-way string quick sort"""

    def __init__(self, str_list):
        """initialization"""

        self.str_list = str_list
        self.sort(0, len(self.str_list) - 1, 0)

    def __str__(self):
        """to string"""

        out = []

        for idx, item in enumerate(self.str_list):
            out.append("#%02d: %s" % (idx, item))

        return "\n".join(out)

    def exchange(self, idx_from, idx_to):
        """exchange index between from/to"""

        curr = self.str_list[idx_from]
        self.str_list[idx_from] = self.str_list[idx_to]
        self.str_list[idx_to] = curr

    def sort(self, idx_st, idx_end, char_idx):
        """sort string"""

        # terminate whtn index overlap
        if idx_st >= idx_end:
            return

        lt = idx_st
        gt = idx_end
        curr_idx = idx_st + 1

        pivot_char = self.str_list[idx_st][char_idx]

        char_found = (pivot_char != None)

        # quick sort by char
        while curr_idx <= gt:
            curr_char = self.str_list[curr_idx][char_idx]

            if curr_char is not None:
                char_found = True

            if curr_char < pivot_char:
                self.exchange(lt, curr_idx)
                lt += 1
                curr_idx += 1

            elif curr_char > pivot_char:
                self.exchange(gt, curr_idx)
                gt -= 1

            else:
                curr_idx += 1

        # return if all strings are out-of-bound
        if not char_found:
            return

        # sort 3 sub-arrays recursively
        self.sort(idx_st, lt - 1, char_idx)
        self.sort(gt + 1, idx_end, char_idx)

        if gt > lt:
            # move commpare index for identical part
            self.sort(lt, gt, char_idx + 1)

if __name__ == "__main__":

    sc_list = StringCustom.random_gen(30, 30)

    radix_sort = Quick3Sort(sc_list)

    print radix_sort
