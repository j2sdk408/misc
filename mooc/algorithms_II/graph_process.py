"""
implementation of graph algorithms
"""

from graph import Graph


class GraphProcess(object):
    """class for graph processing"""

    @staticmethod
    def degree(G, v):
        """compute the degree of v"""

        return len(G.adj(v))

    @staticmethod
    def max_degree(G):
        """compute maximum degree"""

        return max([GraphProcess.degree(G, x) for x in xrange(G.V())])

    @staticmethod
    def average_degree(G):
        """compute average degree"""

        return 2. * G.E() / G.V()

    @staticmethod
    def number_of_self_loops(G):
        """count self-loops"""

        count = 0

        for v in xrange(G.V()):
            if v in G.item_dict[v]:
                count += 1

        return count

    @staticmethod 
    def print_info(G):
        """print graph info"""

        print "max. degree: %d" % GraphProcess.max_degree(G)
        print "avg. degree: %d" % GraphProcess.average_degree(G)
        print "#self-loops: %d" % GraphProcess.number_of_self_loops(G)

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Graph.from_file(file_name)

    GraphProcess.print_info(G)

