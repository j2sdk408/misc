"""
"""

from edge import Edge

class EdgeWeightedGraph(object):
    """class for edge weighted graph"""

    def __init__(self):
        """intializer"""

        self.v_count = 0
        self.item_dict = {}

    @classmethod
    def from_v(cls, v_in):
        """initial graph from v"""

        G = cls()
        G.v_count = v_in

        for v in xrange(v_in):
            G.item_dict[v] = []

        # check graph
        return G

    @classmethod
    def from_file(cls, file_name):
        """initial graph from file"""

        G = None

        with open(file_name, "r") as f:
            for idx, line in enumerate(f):

                if idx == 0:
                    G = cls.from_v(int(line))

                elif idx == 1:
                    e_count = int(line)

                else:
                    v, w, weight = line.split()

                    edge = Edge(int(v), int(w), float(weight))
                    G.add_edge(edge)

        # check graph
        assert G.v_count == len(G.item_dict.keys())
        assert G.E() == e_count

        return G

    def __str__(self):
        """to string"""

        out_list = []

        edge_set = set([])

        for v in self.item_dict:
            edge_set.update(self.item_dict[v])

        for e in edge_set:
            out_list.append(str(e))

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "graph {"

        for e in self.edges():
            e.to_dot()

        print "}"

    def add_edge(self, e):
        """add an edge v->w"""

        v = e.either()
        w = e.other(v)

        # both vertex of the edge has a reference
        self.item_dict[v].append(e)
        self.item_dict[w].append(e)

    def adj(self, v):
        """edges adjacent to v"""

        assert v in self.item_dict
        return self.item_dict[v]

    def edges(self):
        """all edges in this graph"""

        edge_set = set([])

        for v in self.item_dict:
            edge_set.update(self.item_dict[v])

        return edge_set

    def V(self):
        """number of vertices"""

        return self.v_count

    def E(self):
        """number of edges"""

        return sum([len(self.item_dict[x]) for x in self.item_dict]) / 2

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = EdgeWeightedGraph.from_file(file_name)

    print str(G)
    #G.to_dot()

