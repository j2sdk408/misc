"""
implementation for string symbol table with ternary search try
"""

class Node(object):
    """class for tri node"""

    MIDDLE = 0
    LEFT = 1
    RIGHT = 2

    def __init__(self):
        """initialization"""

        self.value = None
        self.char = None

        # 0: middle
        # 1: left
        # 2: right
        self.node_list = [None] * 3

class StringST(object):
    """class for string-based symbol table"""

    def __init__(self):
        """initialization"""

        self.root_node = None

    def __str__(self):
        """to string"""

        out_list = []
        return "\n".join(out_list)

    def put(self, key, value):
        """put key-value pair into the symbol table"""

        assert key.__class__ == str

        self.root_node = self.__class__.put_node(
            self.root_node,
            key,
            value,
            0
        )

    def get(self, key):
        """return value paired with given key"""

        assert key.__class__ == str

        node = self.__class__.get_node(self.root_node, key, 0)

        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):
        """delete key and corresponding value"""

        assert key.__class__ == str
        self.root_node = self.__class__.delete_node(self.root_node, key, 0)

    @classmethod
    def put_node(cls, curr_node, key, value, d):
        """put key value to node, currently scanning position d"""

        curr_char = key[d]

        if curr_node is None:
            curr_node = Node()
            curr_node.char = curr_char

        if curr_char < curr_node.char:
            curr_node.node_list[Node.LEFT] = cls.put_node(
                curr_node.node_list[Node.LEFT],
                key,
                value,
                d
            )
        elif curr_char > curr_node.char:
            curr_node.node_list[Node.RIGHT] = cls.put_node(
                curr_node.node_list[Node.RIGHT],
                key,
                value,
                d
            )
        elif d < len(key) - 1:
            curr_node.node_list[Node.MIDDLE] = cls.put_node(
                curr_node.node_list[Node.MIDDLE],
                key,
                value,
                d + 1
            )            
        else:
            curr_node.value = value

        return curr_node

    @classmethod
    def get_node(cls, curr_node, key, d):
        """get key @ position d"""

        curr_char = key[d]

        if curr_node is None:
            return None

        if curr_char < curr_node.char:
            return cls.get_node(
                curr_node.node_list[Node.LEFT],
                key,
                d
            )
        elif curr_char > curr_node.char:
            return cls.get_node(
                curr_node.node_list[Node.RIGHT],
                key,
                d
            )
        elif d < len(key) - 1:
            return cls.get_node(
                curr_node.node_list[Node.MIDDLE],
                key,
                d + 1
            )            
        else:
            return curr_node

    @classmethod
    def delete_node(cls, curr_node, key, d):
        """delete key and corresponding value"""

        curr_char = key[d]

        if curr_node is None:
            return None

        if curr_char < curr_node.char:
            curr_node.node_list[Node.LEFT] = cls.delete_node(
                curr_node.node_list[Node.LEFT],
                key,
                d
            )
        elif curr_char > curr_node.char:
            curr_node.node_list[Node.RIGHT] = cls.delete_node(
                curr_node.node_list[Node.RIGHT],
                key,
                d
            )
        elif d < len(key) - 1:
            curr_node.node_list[Node.MIDDLE] = cls.delete_node(
                curr_node.node_list[Node.MIDDLE],
                key,
                d + 1
            )            
        else:
            curr_node.value = None

        # check if any link exists in current node
        for node in curr_node.node_list:
            if node is not None:
                return curr_node

        # check if current node holds value
        if curr_node.value is not None:
            return curr_node
        else:
            return None

if __name__ == "__main__":

    st = StringST()

    st.put("shell", 2)
    st.put("apple", 123)
    print st.get("shell")
    print st.get("apple")

    st.delete("shell")

    print st.get("shell")
