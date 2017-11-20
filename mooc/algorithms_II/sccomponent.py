"""
implementation of graph algorithms
"""

from digraph import Digraph
from topo_sort import TopologicalSort


class StrongComponent(object):
    """class for strongly-connected component"""

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

    def to_dot(self):
        """to dot format"""

        def get_color(group_id):

            offset = 16

            level = (float(256 - offset * 2) / self.group_count) * group_id
            level = int(level) + offset

            if group_id & 0x01:
                r_level = level
            else:
                r_level = 128

            if group_id & 0x02:
                g_level = level
            else:
                g_level = 128

            if group_id & 0x04:
                b_level = level
            else:
                b_level = 128
            
            return "#%02X%02X%02X" % (
                r_level, 
                g_level, 
                b_level
            )


        print "digraph {"

        # print node
        for v in self.G.item_dict:
            print "\t\"%s\" [style=filled,color=\"%s\"];" % (
                v, 
                get_color(self.group_map[v])
            )

        # print edge
        for v in self.G.item_dict:
            for w in self.G.item_dict[v]:
                print "\t\"%s\" -> \"%s\";" % (v, w)

        print "}"

    def search(self):
        """search for connected component"""

        self.group_count = 0

        for v in self.reversed_post_order():
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

    def reversed_post_order(self):
        """get reversed-post order of G_reversed"""

        # get reversed-post order of G_reversed
        G_reversed = self.G.reverse()
        order_list = TopologicalSort(G_reversed).order()

        return order_list

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

    G = Digraph.from_file(file_name)

    sc = StrongComponent(G)

    #print str(sc)
    sc.to_dot()

