"""
implementation of graph algorithms
"""

from digraph import Digraph
from dfs_pathes import DfsPathes


class CycleDetect(object):
    """class for cycle detection"""

    def __init__(self, G):
        """initialization"""

        self.G = G
        self.marked_map = {}
        self.edge_to_map = {}

        self.cycle_list = []

        for v in xrange(self.G.V()):
            self.marked_map[v] = False
            self.edge_to_map[v] = None

        self.search()

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("marked: %s" % self.marked_map)
        out_list.append("edge-to: %s" % self.edge_to_map)
        out_list.append("cycle: %s" % self.cycle_list)

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        cycle_map = {}

        for v in xrange(self.G.V()):
            cycle_map[v] = []

        # contruct cycle edge map
        for cycle in self.cycle_list:
            for idx in range(len(cycle) - 1):
                cycle_map[cycle[idx]].append(cycle[idx + 1])

            cycle_map[cycle[-1]].append(cycle[0])

        print "digraph {"

        # print edge
        for v in self.G.item_dict:
            for w in self.G.item_dict[v]:
                if w in cycle_map[v]:
                    print "\t\"%s\" -> \"%s\" [color=\"red\"];" % (v, w)
                else:
                    print "\t\"%s\" -> \"%s\";" % (v, w)

        print "}"

    def search(self):
        """search """

        for v in xrange(self.G.V()):
            if not self.marked_map[v]:
                self.dfs(v)

    def dfs(self, v_in):
        """run DFS"""

        self.marked_map[v_in] = True

        for w in self.G.adj(v_in):
            if not self.marked_map[w]:
                self.edge_to_map[w] = v_in
                self.dfs(w)

            else:
                # check cycle
                self.check_cycle(v_in, w)

    def check_cycle(self, v, w):
        """check cycle between v & w"""

        #print "check: %s->%s" % (v, w)
        edge_list = [v]
        edge = v

        while True:
            #print "%s <- %s" % (edge, self.edge_to_map[edge])
            edge = self.edge_to_map[edge]
            edge_list.append(edge)

            if edge is None:
                break
            elif edge == w:
                self.cycle_list.append(edge_list[::-1])
                break

if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Digraph.from_file(file_name)

    cd = CycleDetect(G)

    #print str(cd)
    cd.to_dot()

