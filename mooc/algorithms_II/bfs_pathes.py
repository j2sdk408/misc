"""
implementation of graph algorithms
"""

from graph import Graph
from pathes import Pathes


class BfsPathes(Pathes):
    """class for BFS"""

    @classmethod
    def from_graph(cls, G, s):
        """initialization"""

        p = cls()

        # initialize BFS data
        p.marked_map = {}
        p.edge_to_map = {}
        p.distance_map = {}

        for v in xrange(G.V()):
            p.marked_map[v] = False
            p.edge_to_map[v] = None
            p.distance_map[v] = 0

        # assign start vertex
        p.s = s
        p.edge_to_map[s] = s
        p.marked_map[s] = True

        # run
        p.bfs(G, s)

        return p

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("marked  : %s" % self.marked_map)
        out_list.append("edge-to : %s" % self.edge_to_map)
        out_list.append("distance: %s" % self.distance_map)

        return "\n".join(out_list)

    def bfs(self, G, v_in):
        """perform DFS search"""

        v_list = [v_in]

        while v_list:
            curr = v_list.pop(0)
            curr_dist = self.distance_map[curr]

            print "%s -> %s" % (curr, G.adj(curr))
    
            for w in G.adj(curr):
                if not self.marked_map[w]:
                    self.edge_to_map[w] = curr
                    self.distance_map[w] = curr_dist + 1
                    self.marked_map[w] = True
                    v_list.append(w)

    def has_path_to(self, v_in):
        """is theree a path from s to v"""

        assert v_in in self.marked_map
        return self.marked_map[v_in]

    def path_to(self, v_in):
        """path from s to v; null if no such path"""
        
        assert v_in in self.edge_to_map

        if self.edge_to_map[v_in] is None:
            return None

        else:
            # search backwards
            out_list = []

            curr_node = v_in

            while True:
                out_list.append(curr_node)
                if curr_node == self.s:
                    break
                else:
                    curr_node = self.edge_to_map[curr_node]

            return out_list


if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = Graph.from_file(file_name)
    P = BfsPathes.from_graph(G, 0)

    print str(P)

    P.print_path(G.V())

