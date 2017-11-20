"""
implementation of graph algorithms
"""

from graph import Graph


class Connected_component(object):
    """class for connected component"""

    def __init__(self, G):
        """initialization"""

        self.marked_map = {}
        self.group_map = {}
        self.group_count = 0

        self.G = G

        for v in range(G.V()):
            self.marked_map[v] = False
            self.group_map[v] = None

        self.search()

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("marked: %s" % self.marked_map)
        out_list.append("group : %s" % self.group_map)
        out_list.append("#group : %s" % self.group_count)

        return "\n".join(out_list)

    def search(self):
        """search for connected component"""

        self.group_count = 0

        for v in xrange(G.V()):
            if not self.marked_map[v]:
                self.dfs(v)
                self.group_count += 1

    def dfs(self, v_in):
        """run DFS"""

        self.marked_map[v_in] = True
        self.group_map[v_in] = self.group_count

        for w in self.G.adj(v_in):
            if not self.marked_map[w]:
                self.dfs(w)

    def connected(self, v, w):
        """are v and w connected?"""

        return self.group_map[v] == self.group_map[w]

    def count(self):
        """number of connected components"""

        return self.group_count

    def id(self, v):
        """component identifier for v"""

        return self.group_map[w]

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Graph.from_file(file_name)

    cc = Connected_component(G)

    print str(cc)

