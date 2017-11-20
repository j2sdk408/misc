"""
implementation of graph algorithms
"""

from digraph import Digraph
from dfs_pathes import DfsPathes


class TopologicalSort(object):
    """class for topological sort"""

    def __init__(self, G):
        """initialization"""

        self.marked_map = {}
        self.reverse_list = []

        for v in xrange(G.V()):
            self.marked_map[v] = False

        self.search(G)

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("marked: %s" % self.marked_map)
        out_list.append("reverse: %s" % self.reverse_list)

        return "\n".join(out_list)

    def order(self):
        """get topological order"""

        return self.reverse_list[::-1]

    def search(self, G):
        """search"""

        for v in xrange(G.V()):
            if not self.marked_map[v]:
                self.dfs(G, v)

    def dfs(self, G, v_in):
        """run DFS"""

        self.marked_map[v_in] = True

        for w in G.adj(v_in):
            if not self.marked_map[w]:
                self.dfs(G, w)

        #print "add: %s" % v_in
        self.reverse_list.append(v_in)

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Digraph.from_file(file_name)

    ts = TopologicalSort(G)

    print str(ts)

