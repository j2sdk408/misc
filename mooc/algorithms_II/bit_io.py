"""
implementation of bit I/O
"""

class BitIO(object):
    """class for bit input/output"""

    def __init__(self, file_name, mode):
        """initializer"""

        self.mode = mode
        assert self.mode in ["w", "r"]

        self.file_name = file_name
        self.buffer = []

    def __enter__(self):
        """acquire file"""

        # perform file I/O in binary mode
        if self.mode == "r":
            self.file_handle = open(self.file_name, "rb")
        else:
            self.file_handle = open(self.file_name, "wb")

        return self

    def __exit__(self, *args):
        """release file"""

        if self.mode == "w":
            # flush buffer
            self.write_bits(
                len(self.buffer), 
                self.to_int(self.buffer)
            )

        self.file_handle.close()

    @staticmethod
    def to_int(bit_list):
        """convert bit list to int"""

        value = 0
        power = 2 ** (len(bit_list) - 1)

        for bit in bit_list:
            value += power * bit
            power /= 2

        return value

    @staticmethod
    def to_bit_list(value):
        """convert int to bit list"""

        assert value >= 0 and value < 256

        bit_list = []
        power = 2 ** 7

        for _ in xrange(8):
            if value & power != 0:
                bit_list.append(1)
            else:
                bit_list.append(0)

            power /= 2

        return bit_list

    def read_char(self):
        """read 8 bits of data and returen as a char value"""

        assert self.mode == "r"
        return self.read_bits(8)

    def write_char(self, value):
        """write 8 bits of data"""

        assert self.mode == "w"
        self.write_bits(8, value)

    def read_bits(self, n):
        """read n bits of data and returen as a char value"""

        assert self.mode == "r"

        if n > len(self.buffer):
            # calcuate total amount of bytes need to be read
            bit_length = n - len(self.buffer)

            byte_length = bit_length / 8
            if bit_length % 8 != 0:
                byte_length += 1

            for _ in xrange(byte_length):
                value = self.file_handle.read(1)
                assert value != ""
                self.buffer += self.to_bit_list(ord(value))

        value = self.to_int(self.buffer[:n])
        self.buffer = self.buffer[n:]
        return value

    def write_bits(self, n, value):
        """write n bits(lsb) of data"""

        assert self.mode == "w"
        assert (2 ** n) > value

        if n > 8:
            mod = 2 ** (n / 2)
            self.write_bits(n - n / 2, value / mod)
            self.write_bits(n / 2, value % mod)

        else:
            assert value >= 0 and value < 256

            bit_list = self.to_bit_list(value)
            self.buffer += bit_list[-n:]

            while len(self.buffer) > 8:
                value = self.to_int(self.buffer[:8])
                self.buffer = self.buffer[8:]
                self.file_handle.write(chr(value))

    def is_empty(self):
        """is the bitstream empty?"""

        assert self.mode == "r"

        # not empty if there's value in buffer
        if self.buffer:
            return False

        # read from file and put into buffer
        value = self.file_handle.read(1)

        if value != "":
            self.buffer += self.to_bit_list(ord(value))

        # check buffer status
        if self.buffer:
            return False

        return True


if __name__ == "__main__":

    input_name = "abra.txt"
    output_name = "out.txt"


    with BitIO(input_name, "r") as bi:
        with BitIO(output_name, "w") as bo:

            while not bi.is_empty():
                value = bi.read_char()
                bo.write_char(value)

