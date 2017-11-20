"""
implementation of Ford-Fulkerson algorithm
"""

import Queue
from flow_network import FlowNetwork

class FFson(object):
    """class for Ford-Fulkerson"""

    def __init__(self, G, s, t):
        """initialization"""

        self._G = G
        self._s = s
        self._t = t

        self._marked_map = {}
        self._edge_to_map = {}
        self._value = 0

        self._min_cut_list = []

        self.max_flow()
        self.min_cut()

    def __str__(self):
        """to string"""

    def to_dot(self):
        """to dot format"""

        print "digraph {"

        for v in self._min_cut_list:
            print "\t\"%s\"[color=\"red\"]" % v

        for e in self._G.edges():
            v = e.v_from()
            w = e.v_to()

            print "\t\"%s\" -> \"%s\" [label=\"%s/%s\", penwidth=%s];" % (
                v, 
                w, 
                e.flow(),
                e.capacity(),
                0.1 + e.flow() * 0.2,
            )

        print "}"

    def max_flow(self):
        """search for max flow"""

        self._value = 0

        while self.has_aug_path():
            bottle = float("inf")

            # compute bottleneck capacity
            curr_v = self._t

            while curr_v != self._s:
                curr_resid = self._edge_to_map[curr_v].residual_to(curr_v)
                bottle = min(bottle, curr_resid)

                curr_v = self._edge_to_map[curr_v].other(curr_v)

            # update augment flow
            curr_v = self._t

            while curr_v != self._s:
                self._edge_to_map[curr_v].add_flow_to(curr_v, bottle)
                
                curr_v = self._edge_to_map[curr_v].other(curr_v)

            self._value += bottle

    def min_cut(self):
        """search for min-cut"""

        # reset data structure
        for v in xrange(G.V()):
            self._marked_map[v] = False

        self._min_cut_list = []

        queue = Queue.Queue()

        queue.put(self._s)
        self._marked_map[self._s] = True
        self._min_cut_list.append(self._s)

        while not queue.empty():
            curr_v = queue.get()

            # breath-first search implementation
            for e in self._G.adj(curr_v):
                w = e.other(curr_v)

                if not self._marked_map[w] and e.residual_to(w) > 0:
                    self._marked_map[w] = True
                    queue.put(w)
                    self._min_cut_list.append(w)

    def has_aug_path(self):
        """has augmenting path from s to t"""

        # reset data structure
        for v in xrange(G.V()):
            self._marked_map[v] = False
            self._edge_to_map[v] = None

        queue = Queue.Queue()

        # starts with vertex s
        queue.put(self._s)
        self._marked_map[self._s] = True

        while not queue.empty():
            curr_v = queue.get()

            # breath-first search implementation
            for e in self._G.adj(curr_v):
                w = e.other(curr_v)

                if not self._marked_map[w] and e.residual_to(w) > 0:
                    self._edge_to_map[w] = e
                    self._marked_map[w] = True
                    queue.put(w)

        return self._marked_map[self._t]

    def value(self):
        """flow value"""

        return self._value

    def in_cut(self, v_in):
        """is v_in reachable from s in residual network?"""

        assert v_in in self._marked_map
        return self._marked_map[v_in]


if __name__ == "__main__":

    import sys
    file_name = sys.argv[1]

    G = FlowNetwork.from_file(file_name)

    ff = FFson(G, 0, 7)

    ff.to_dot()
