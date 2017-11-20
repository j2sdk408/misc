"""
implementation of graph algorithms
"""

class Pathes(object):
    """class for path searching"""

    def __init__(self):
        """initializer"""

        self.s = 0

    @classmethod
    def from_graph(cls, G, s):
        """find pathes in G grom source s"""

        p = cls()
        p.s = s

        assert s < G.V()
        assert s >= 0
        return p

    def has_path_to(self, v_in):
        """is theree a path from s to v"""

        return False

    def path_to(self, v_in):
        """path from s to v; null if no such path"""

        return None

    def print_path(self, v_count):
        """print path"""

        for v in xrange(v_count):
            print "%s: %s" % (v, self.path_to(v))


if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Graph.from_file(file_name)

    P = Pathes.from_graph(G, 0)

