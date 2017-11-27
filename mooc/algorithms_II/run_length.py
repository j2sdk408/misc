"""
implementation of run length encoding
"""

from bit_io import BitIO


class RunLength(object):
    """class for run-length encoding"""

    JUMP_MAP = {
        0: 1,
        1: 0
    }

    def __init__(self, in_name, out_name):
        """initialization"""

        self.max_count = 256
        self.bit_lenth = 8

        self.in_name = in_name
        self.out_name = out_name

    def compress(self):
        """compress"""

        curr_bit = 0
        count = 0

        with BitIO(self.out_name, "w") as bo:
            with BitIO(self.in_name, "r") as bi:

                while not bi.is_empty():

                    if bi.read_bits(1) == curr_bit:
                        count += 1

                        # check if max count reached
                        if count + 1 >= self.max_count:
                            bo.write_char(count)
                            curr_bit = self.JUMP_MAP[curr_bit]
                            count = 0
                    else:
                        # flush count on bit change
                        bo.write_char(count)
                        curr_bit = self.JUMP_MAP[curr_bit]

                        # count for current value
                        count = 1

    def expand(self):
        """compress"""

        curr_bit = 0

        with BitIO(self.out_name, "w") as bo:
            with BitIO(self.in_name, "r") as bi:

                while not bi.is_empty():
                    # read 8-bit count from standard input
                    run = bi.read_char()

                    # write repeated bits
                    for _ in xrange(run):
                        bo.write_bits(1, curr_bit)

                    # toggle bit
                    curr_bit = self.JUMP_MAP[curr_bit]


if __name__ == "__main__":

    import sys

    in_file = sys.argv[1]
    out_file = "%s.bin" % in_file

    co = RunLength(in_file, out_file)
    co.compress()

