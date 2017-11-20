"""
implementation for union find
"""

class UnionFind(object):
    """class for union find"""

    def __init__(self, v_count):
        """initialization"""

        self.item_map = {}

        for idx in xrange(v_count):
            self.item_map[idx] = idx

    def connected(self, v, w):
        """check if v & w is connected"""

        return self.get_root(v) == self.get_root(w)

    def union(self, v, w):
        """add v & w connection"""

        v_root = self.get_root(v)
        w_root = self.get_root(w)

        self.item_map[v_root] = w_root

    def get_root(self, v_in):
        """get root for vertex, with path compression"""

        assert v_in in self.item_map
        v = v_in
        v_list = []
        
        # get_root for root
        while v != self.item_map[v]:
            v_list.append(v)
            v = self.item_map[v]

        # path compression
        for path_v in v_list:
            self.item_map[path_v] = v

        return v

