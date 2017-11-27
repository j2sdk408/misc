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
    """class for Huffman compress algorithm"""

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
            char = bi.read_char()
            return Node(char, 0, None, None)

        else:
            # 0 -> node
            left_node = self.read_try(bi)
            right_node = self.read_try(bi)
            return Node("", 0, left_node, right_node)

    def write_try(self, bo, node):
        """write try"""

        if node.is_leaf():
            # 1 -> leaf
            bo.write_bits(1, 1)
            bo.write_char(node.char)

        else:
            # 0 -> node
            bo.write_bits(1, 0)
            self.write_try(bo, node.left)
            self.write_try(bo, node.right)

    def build_try(self):
        """build try"""

        queue_p = Queue.PriorityQueue()

        # count frequency
        freq_list = [0] * self.char_max
        char_count = 0

        with BitIO(self.in_name, "r") as bi:
            while not bi.is_empty():
                char = bi.read_bits(self.char_size)
                freq_list[char] += 1
                char_count += 1

        # initialize PQ with singleton tries
        for char in xrange(self.char_max):
            freq = freq_list[char]

            if freq != 0:
                curr_node = Node(char, freq, None, None)
                queue_p.put(
                    (curr_node.freq, curr_node)
                )

        while queue_p.qsize() > 1:
            # get 2 nodes with least frequency
            _, x = queue_p.get()
            _, y = queue_p.get()

            # merge nodes
            parent_node = Node("", x.freq + y.freq, x, y)

            queue_p.put(
                (parent_node.freq, parent_node)
            )

        root_node = queue_p.get()[1]

        return (root_node, char_count)

    def build_symbol_table(self, node):
        """build symbol table from root node"""

        st_dict = {}

        # data structure
        # [(code list, node), ...]
        search_stack = [([], node)]

        while search_stack:
            curr_code, curr_node = search_stack.pop()

            if curr_node.is_leaf():
                st_dict[curr_node.char] = curr_code

            else:
                if curr_node.right is not None:
                    search_stack.append((curr_code + [1], curr_node.right))
                if curr_node.left is not None:
                    search_stack.append((curr_code + [0], curr_node.left))

        return st_dict

    def compress(self):
        """compress"""

        # build try
        print "building try..."
        root, char_count = self.build_try()

        # construct loop-up table
        print "building symbol table..."
        st_dict = self.build_symbol_table(root)

        with BitIO(self.out_name, "w") as bo:
            # write tries and character count first
            print "writing try..."
            self.write_try(bo, root)
            bo.write_bits(self.char_count_bits, char_count)

            # write chars by symbol table loop-up
            with BitIO(self.in_name, "r") as bi:
                for _ in xrange(char_count):
                    char = bi.read_bits(self.char_size)

                    # write corresponding code
                    bit_list = st_dict[char]

                    for item in bit_list:
                        bo.write_bits(1, item)

    def expand(self):
        """expand"""

        with BitIO(self.out_name, "w") as bo:
            with BitIO(self.in_name, "r") as bi:

                # read encoding try
                print "reading try..."
                root = self.read_try(bi)

                # read number of chars
                count = bi.read_bits(self.char_count_bits)
                print "reading char count = %s..." % count

                print "expanding..."
                for _ in xrange(count):
                    # search for leaf node
                    x = root

                    while not x.is_leaf():
                        if not bi.read_bits(1):
                            # 0 -> left
                            x = x.left
                        else:
                            # 1 -> right
                            x = x.right

                    assert x.char

                    bo.write_bits(self.char_size, x.char)

if __name__ == "__main__":

    import sys

    in_file = "synsets.txt"
    out_file = "synsets.txt.bin"

    # compress
    #co = Huffman(in_file, out_file)
    #co.compress()

    # expand
    co = Huffman(out_file, out_file + ".txt")
    co.expand()
