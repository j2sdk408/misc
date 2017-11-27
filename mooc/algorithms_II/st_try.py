"""
implementation for string symbol table
"""

import Queue

class Node(object):
    """class for tri node"""

    CHAR_RANGE = 256

    def __init__(self):
        """initialization"""

        self.value = None
        self.node_list = [None] * self.CHAR_RANGE

class StringST(object):
    """class for string-based symbol table"""

    def __init__(self):
        """initialization"""

        self.root_node = Node()

    def __str__(self):
        """to string"""

        out_list = []

        node_queue = [self.root_node]
        level = 0

        while node_queue:
            curr_list = []

            for node in node_queue:
                for idx, node_link in enumerate(node.node_list):
                    if node_link is not None:
                        out_list.append("%s-> %s" % (" " * level, chr(idx)))
                        curr_list.append(node_link)

            node_queue = curr_list
            level += 1

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

        if curr_node is None:
            curr_node = Node()

        if d == len(key):
            curr_node.value = value
            return curr_node

        else:
            node_idx = ord(key[d])

            curr_node.node_list[node_idx] = cls.put_node(
                curr_node.node_list[node_idx],
                key,
                value,
                d + 1
            )

            return curr_node

    @classmethod
    def get_node(cls, curr_node, key, d):
        """get key @ position d"""

        if curr_node is None:
            return None

        if d == len(key):
            return curr_node

        else:
            node_idx = ord(key[d])

            return cls.get_node(
                curr_node.node_list[node_idx],
                key,
                d + 1
            )

    @classmethod
    def delete_node(cls, curr_node, key, d):
        """delete key and corresponding value"""

        if curr_node is None:
            return None

        if d == len(key):
            curr_node.value = None

        else:
            node_idx = ord(key[d])

            curr_node.node_list[node_idx] = cls.delete_node(
                curr_node.node_list[node_idx],
                key,
                d + 1
            )

        # check if any link exists in current node
        for node_link in curr_node.node_list:
            if node_link is not None:
                return curr_node

        # check if current node holds value
        if curr_node.value is not None:
            return curr_node
        else:
            return None

    def keys(self):
        """get in-order key list"""

        key_list = []
        self.collect(self.root_node, "", key_list)
        return key_list

    def keys_with_prefix(self, prefix):
        """search keys with prefix"""

        node = self.get_node(self.root_node, prefix, 0)
        
        key_list = []
        self.collect(node, prefix, key_list)
        return key_list

    @classmethod
    def collect(cls, curr_node, str_prefix, key_list):
        """collect strings below node, with prefix string"""

        if curr_node is None:
            return

        if curr_node.value is not None:
            key_list.append(str_prefix)

        for idx, node_link in enumerate(curr_node.node_list):
            cls.collect(node_link, str_prefix + chr(idx), key_list)

    def longest_prefix_of(self, query):
        """search for longest prefix in query string"""

        length = self.search(self.root_node, query, 0, 0)
        return query[:length]

    @classmethod
    def search(cls, curr_node, query, d, length):
        """search for the length of longest prefix"""

        if curr_node is None:
            return length

        if curr_node.value is not None:
            length = d

        if d == len(query):
            return length

        curr_char = ord(query[d])

        return cls.search(
            curr_node.node_list[curr_char], 
            query, 
            d + 1, 
            length
        )

if __name__ == "__main__":

    st = StringST()

    st.put("shell", 2)
    st.put("so", 2)
    st.put("share", 2)
    st.put("shelter", 20)
    st.put("apple", 3)

    print st.longest_prefix_of("sort")

