"""
class for single-source shortest paths
"""

import Queue
from ewdigraph import EdgeWeightedDigraph
from union_find import UnionFind


class ShortestPath(object):
    """class for shortest path"""

    def __init__(self, G, s):
        """initialization"""

        self.G = G
        self.s = s

        self.edge_to_map = {}
        self.dist_map = {}

        for v in xrange(self.G.V()):
            self.edge_to_map[v] = None
            self.dist_map[v] = float("inf")

        self.search()

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("edge-to: %s" % self.edge_to_map)
        out_list.append("length: %s" % self.dist_map)

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

    def search(self):
        """search for MST"""

        search_queue = Queue.Queue()

        # starts with s
        search_queue.put(self.s)
        self.dist_map[self.s] = 0

        while not search_queue.empty():

            curr_v = search_queue.get()

            for e in self.G.adj(curr_v):
                w = e.v_to()
                new_len = self.dist_map[curr_v] + e.weight

                # edge relaxation
                if new_len < self.dist_map[w]:
                    self.edge_to_map[w] = e
                    self.dist_map[w] = new_len

                    search_queue.put(w)

    def dist_to(self, v_in):
        """length of shortest path from s to v"""

        if not self.has_path_to(v_in):
            return None

        return self.dist_map[v_in]

    def path_to(self, v_in):
        """shortest path from s to v"""

        if not self.has_path_to(v_in):
            return None

        if v_in == self.s:
            return None

        # search backwards
        out_list = []

        curr_v = v_in

        while True:
            curr_e = self.edge_to_map[curr_v]

            out_list.append(curr_e)

            if curr_e.v_from() == self.s:
                break

            else:
                curr_v = self.edge_to_map[curr_v].v_from()

        # print log
        for e in out_list:
            print str(e)

        print "length = %s (check = %s)" % (
            self.dist_map[v_in],
            sum([x.weight for x in out_list])
        )

        return out_list

    def has_path_to(self, v_in):
        """has a path from s to v"""

        return self.dist_map[v_in] != float("inf")

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = EdgeWeightedDigraph.from_file(file_name)

    sp = ShortestPath(G, 0)

    for v in xrange(G.V()):
        print "path to: %s" % v
        sp.path_to(v)
        print
