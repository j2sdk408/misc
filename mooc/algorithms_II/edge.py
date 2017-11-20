"""class for edge
"""

class Edge(object):
    """class for edge"""

    def __init__(self, v, w, weight):
        """initialization"""

        self.v = v
        self.w = w
        self.weight = weight

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append("%s -- %s (%s)" % (self.v, self.w, self.weight))

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "\t\"%s\" -- \"%s\" [label = \"%s\"];" % (
            self.v, 
            self.w,
            self.weight
        )

    def either(self):
        """either endpoint"""

        return self.v

    def other(self, v_in):
        """the endpoint that's not v"""

        assert v_in in [self.v, self.w]

        if v_in == self.v:
            return self.w
        else:
            return self.v

    def compare_to(self, edge_in):
        """cpmare this edge to that edge"""

        if self.weight < edge_in.weight:
            return -1
        elif self.weight > edge_in.weight:
            return 1
        else:
            return 0

if __name__ == "__main__":

    e1 = Edge(1, 2, 4)
    e2 = Edge(1, 2, 3)

    print str(e1)
    print str(e2)
    print e1.compare_to(e2)

    print e1.either()
    print e1.other(e1.either())
