"""
implementation of binary dump
"""

import PIL.Image

class BitDump(object):
    """class for binary dump"""

    def __init__(self):
        """initialization"""

        self.bin_length = 16
        self.hex_length = 4
        self.bmp_length = 16
        self.bmp_pixel = 4

    @staticmethod
    def get_bit_list(input_str):
        """get bit list from input string"""

        out_list = []

        for char in input_str:
            value = ord(char)

            for bit_idx in xrange(8):
                if value & (0x80 >> bit_idx) != 0:
                    out_list.append(1)
                else:
                    out_list.append(0)

        return out_list

    @staticmethod
    def get_byte_list(input_str):
        """get byte list from input string"""

        out_list = []

        for char in input_str:
            out_list.append(ord(char))

        return out_list

    def convert_bin(self, input_str):
        """convert input string to 0/1s"""

        out_list = self.get_bit_list(input_str)

        # re-organize output
        curr_idx = 0

        while curr_idx + self.bin_length < len(out_list):
            curr_list = out_list[curr_idx: curr_idx + self.bin_length]
            print "".join([str(x) for x in curr_list])
            curr_idx += self.bin_length

        if curr_idx != len(out_list):
            print "".join([str(x) for x in out_list[curr_idx:]])

        print "%d bits" % len(out_list)

    def convert_hex(self, input_str):
        """convert input string to hex"""

        out_list = self.get_byte_list(input_str)

        # re-organize output
        curr_idx = 0

        while curr_idx + self.hex_length < len(out_list):
            curr_list = out_list[curr_idx: curr_idx + self.hex_length]
            print " ".join([("%02X" % x) for x in curr_list])
            curr_idx += self.hex_length

        if curr_idx != len(out_list):
            print " ".join([("%02X" % x) for x in out_list[curr_idx:]])

        print "%d bytes" % len(out_list)

    def convert_bmp(self, input_str):
        """convert input string to bitmap picture"""

        out_list = self.get_bit_list(input_str)

        # re-organize output
        # output data
        width = self.bmp_length
        height = len(out_list) / self.bmp_length

        if len(out_list) % self.bmp_length != 0:
            height += 1

        im_out = PIL.Image.new("RGB", (width, height))

        # re-format data
        data_out = []
        for item in out_list:
            if item:
                # 1s as black pixel
                data_out.append((0, 0, 0))
            else:
                # 0s as white pixel
                data_out.append((255, 255, 255))

        # padding with red pixels
        if len(out_list) != width * height:
            data_out += [(255, 0, 0)] * (width * height - len(out_list))

        im_out.putdata(data_out)
        im_out.save("out.bmp")

        print "%d bits" % len(out_list)


if __name__ == "__main__":

    import sys

    file_name = sys.argv[1]

    dump = BitDump()

    with open(file_name, "rb") as f:
        raw = f.read()

    # dumping bits
    print "binary:"
    dump.convert_bin(raw)
    print "hex:"
    dump.convert_hex(raw)
    print "bmp:"
    dump.convert_bmp(raw)
