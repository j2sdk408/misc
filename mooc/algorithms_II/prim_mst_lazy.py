"""
"""

import Queue
from ewgraph import EdgeWeightedGraph


class PrimLazyMST(object):
    """class for minimum-spanning tree"""

    def __init__(self, G):
        """initialization"""

        self.G = G
        self.edge_list = []
        self.marked_map = {}

        # build pirority queue
        self.edge_queue = Queue.PriorityQueue()

        for v in xrange(self.G.V()):
            self.marked_map[v] = False

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

        # start form vertex 0
        self.visit(0)

        while not self.edge_queue.empty() and \
              len(self.edge_list) < self.G.V() - 1:

            # search for the next outside edge with minimum weight
            while True:
                _, new_edge = self.edge_queue.get()
                new_v = new_edge.either()
                new_w = new_edge.other(new_v)

                if not self.marked_map[new_v]:
                    break
                if not self.marked_map[new_w]:
                    new_v = new_w
                    break

            # add new edge & v
            self.edge_list.append(new_edge)
            self.visit(new_v)

    def visit(self, v_in):
        """add v-related edges to edge queue"""

        self.marked_map[v_in] = True

        for e in self.G.adj(v_in):
            if not self.marked_map[e.other(v_in)]:
                self.edge_queue.put((e.weight, e))

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

    mst = PrimLazyMST(G)

    #print mst.edges()
    print str(mst)

    #mst.to_dot()


