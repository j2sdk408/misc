"""
implementation of run length encoding
"""

from bit_io import BitIO


class RunLength(object):
    """class for run-length encoding"""

    def __init__(self):
        """initialization"""

        self.max_count = 256
        self.bit_lenth = 8

    def compress(self, bi):
        """compress"""

        bit_map = {
            0: 1, 
            1: 0
        }
        curr_bit = 0
        count = 0

        with BitIo("compress.txt", "w") as bo:

            while not bi.is_empty():

                if bi.read_bits(1) == curr_bit:
                    count += 1

                    # check if max count reached
                    if count + 1 >= self.max_count:
                        bo.write_char(count)
                        curr_bit = bit_map[curr_bit]
                        count = 0
                else:
                    # flush count on bit change
                    bo.write_char(count)
                    curr_bit = bit_map[curr_bit]

                    # count for current value
                    count = 1
                        
    def expand(self, bi):
        """compress"""

        bit_map = {
            0: 1, 
            1: 0
        }
        curr_bit = 0

        with BitIO("expand.txt", "w") as bo:
            while not bi.is_empty():
                # read 8-bit count from standard input
                run = bi.read_char()

                # write repeated bits
                for _ in xrange(run):
                    bo.write_bits(1, curr_bit)

                # toggle bit
                curr_bit = bit_map[curr_bit]


if __name__ == "__main__":

    rl = RunLength()

    with BitIO("out.txt", "r") as bi:
        rl.expand(bi)
