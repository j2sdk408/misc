"""
"""

import Queue
from ewgraph import EdgeWeightedGraph
from union_find import UnionFind


class KruskalMST(object):
    """class for minimum-spanning tree"""

    def __init__(self, G):
        """initialization"""

        self.G = G
        self.edge_list = []

        self.search()

    def __str__(self):
        """to string"""

        out_list = []

        for e in self.edge_list:
            v = e.either()
            w = e.other(v)
            out_list.append("%s -- %s (%s)" % (v, w, e.weight))

        out_list.append("Total = %s" % self.weight())

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "graph {"

        for e in self.G.edges():
            v = e.either()
            w = e.other(v)
            if e in self.edge_list:
                print "\t\"%s\" -- \"%s\" [label = \"%s\", penwidth=5];" % (v, w, e.weight)
            else:
                print "\t\"%s\" -- \"%s\" [label = \"%s\"];" % (v, w, e.weight)

        print "}"

    def search(self):
        """search for MST"""

        # build pirority queue
        edge_queue = Queue.PriorityQueue()

        for e in self.G.edges():
            edge_queue.put((e.weight, e))

        uf = UnionFind(self.G.V())

        while not edge_queue.empty() and \
              len(self.edge_list) < self.G.V() - 1:

            # greedily add edges to MST
            _, e = edge_queue.get()
            v = e.either()
            w = e.other(v)

            # check if edge v-w not create cycle
            if not uf.connected(v, w):
                # merge sets
                uf.union(v, w)

                # add edge
                self.edge_list.append(e)

    def edges(self):
        """edges in MST"""

        return self.edge_list

    def weight(self):
        """wieght of MST"""

        return sum([x.weight for x in self.edge_list])


if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = EdgeWeightedGraph.from_file(file_name)

    mst = KruskalMST(G)

    print str(mst)

