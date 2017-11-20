"""class for directed edge
"""

class DirectedEdge(object):
    """class for edge"""

    def __init__(self, v, w, weight):
        """initialization"""

        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("%s -> %s (%s)" % (self.v, self.w, self.weight))

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "\t\"%s\" -> \"%s\" [label = \"%s\"];" % (
            self.v, 
            self.w,
            self.weight
        )

    def v_from(self):
        """either endpoint"""

        return self.v

    def v_to(self):
        """the endpoint that's not v"""

        return self.w

    def compare_to(self, edge_in):
        """cpmare this edge to that edge"""

        if self.weight < edge_in.weight:
            return -1
        elif self.weight > edge_in.weight:
            return 1
        else:
            return 0

    def reverse(self):
        """return reversed edge"""

        return self.__class__(self.w, self.v, self.weight)

if __name__ == "__main__":

    e1 = DirectedEdge(1, 2, 4)
    e2 = DirectedEdge(1, 2, 3)

    print str(e1)
    print str(e2)
    print e1.compare_to(e2)

