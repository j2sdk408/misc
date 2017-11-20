"""
implementation of graph algorithms
"""


class Graph(object):
    """class for graph"""

    def __init__(self):
        """intializer"""

        self.v_count = 0
        self.e_count = 0
        self.item_dict = {}

    @classmethod
    def from_v(cls, v_in):
        """initial graph from v"""

        G = cls()
        G.v_count = v_in

        for v in xrange(v_in):
            G.item_dict[v] = []

        # check graph
        assert G.v_count == len(G.item_dict.keys())
        assert G.e_count * 2 == sum([len(G.item_dict[x]) for x in G.item_dict])
        return G

    @classmethod
    def from_file(cls, file_name):
        """initial graph from file"""

        G = cls()

        with open(file_name, "r") as f:
            for idx, line in enumerate(f):

                if idx == 0:
                    G.v_count = int(line)

                    for v in xrange(G.v_count):
                        G.item_dict[v] = []

                elif idx == 1:
                    G.e_count = int(line)

                else:
                    v, w = line.split()
                    G.add_edge(int(v), int(w))

        # check graph
        assert G.v_count == len(G.item_dict.keys())
        assert G.e_count * 2 == sum([len(G.item_dict[x]) for x in G.item_dict])

        return G

    def __str__(self):
        """to string"""

        out_list = []

        for v in xrange(self.V()):
            for w in self.adj(v):
                out_list.append("%s-%s" % (v, w))

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "graph {"
        for v in self.item_dict:
            for w in self.item_dict[v]:
                print "\t\"%s\" -- \"%s\";" % (v, w)
        print "}"

    def add_edge(self, v, w):
        """add an edge v-w"""

        self.item_dict[v].append(w)
        self.item_dict[w].append(v)

    def adj(self, v):
        """vertices adjacent to v"""

        assert v in self.item_dict
        return self.item_dict[v]

    def V(self):
        """number of vertices"""

        return self.v_count

    def E(self):
        """number of edges"""

        return self.e_count



if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Graph.from_file(file_name)

    print str(G)

