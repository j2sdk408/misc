"""
implementation for Huffman compression
"""

import Queue
from bit_io import BitIO

class Node(object):
    """class for Huffman nodes
    binary try, with character in leaf nodes
    """

    def __init__(self, char, freq, left, right):
        """initializer"""

        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        """is leaf node"""

        return self.left is None and self.right is None

class Huffman(object):

    def __init__(self, in_name, out_name):
        """initialization"""

        self.in_name = in_name
        self.out_name = out_name

        self.char_size = 8
        self.char_max = 2 ** self.char_size
        self.char_count_bits = 32

    def read_try(self, bi):
        """read try
        node separator: 0
        leaf separator: 1
        """

        if bi.read_bits(1):
            # 1 -> leaf
            c = bi.read_char()
            return Node(chr(c), 0, None, None)

        else:
            # 0 -> node
            x = self.read_try(bi)
            y = self.read_try(bi)
            return Node("", 0, x, y)

    def write_try(self, bo, node):
        """write try"""

        if node.is_leaf():
            # 1 -> leaf
            bo.write_bits(1, 1)
            bo.write_char(node.char)

        else:
            # 0 -> node
            bo.write(1, 0)
            self.write_try(bo, node.left)
            self.write_try(bo, node.right)

    def build_try(self):
        """build try"""

        queue_p = Queue.PriorityQueue()

        # count frequency
        freq_list = [0] * self.char_max
        char_count = 0

        with BitIO(self.in_name, "r") as bi:
            char = bi.read_bits(self.char_size)
            freq_list[char] += 1
            char_count += 1

        # initialize PQ with singleton tries
        for char in xrange(self.char_max):
            freq = freq_list[char]

            if freq != 0:
                curr_node = Node(str(char), freq, None, None)
                quene.put(
                    (curr_node.freq, curr_node)
                )

        while queue_p.qsize() > 1:
            # get 2 nodes with least frequency
            x = queue_p.get()
            y = queue_p.get()

            # merge nodes
            parent_node = Node("", x.freq + y.freq, x, y)

            queue_p.put(
                (parent_node.freq, parent_node)
            )

        return (queue_p.get(), char_count)

    def build_symbol_table(self, node):
        """build symbol table from root node"""

        return {}

    def compress(self):
        """compress"""

        # build try
        root, char_count = self.build_try()

        # construct loop-up table
        code_table = self.build_symbol_table(root)

        with BitIO(self.out_name, "w") as bo:
            # write tries and character count first
            self.write_try(bo, root)
            bo.write_bits(char_count_bits, char_count)
        
            # write chars by symbol table loop-up
            with BitIO(self.in_name, "r") as bi:
                for _ in xrange(char_count):
                    char = bi.read_bits(self.char_size)
                    bit_count, value = code_table[char]

                    bo.write_bits(bit_count, value)

    def expand(self):
        """expand"""

        with BitIO(self.out_name, "w") as bo:
            with BitIO(self.in_name, "r") as bi:

                # read encoding try
                root = self.read_try(bi)

                # read number of chars
                count = bi.read_bits(char_count_bits) 

                for idx in xrange(count):
                    # search for leaf node
                    x = root

                    while not x.is_leaf():
                        if not bi.read_bit(1):
                            # 0 -> left
                            x = x.left
                        else:
                            # 1 -> right
                            x = x.right

                    assert x.char

                    bo.write_bits(self.char_size, x.char)
        

    

