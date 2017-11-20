"""class for flow edge
"""

class FlowEdge(object):
    """class for edge"""

    def __init__(self, v, w, capacity):
        """initialization"""

        self.v = v
        self.w = w
        self._capacity = capacity
        self._flow = 0

    def __str__(self):
        """to string"""

        out_list = []

        out_list.append(
            "%s -- %s (%s/%s)" % (
                self.v, 
                self.w, 
                self._flow,
                self._capacity
            )
        )

        return "\n".join(out_list)

    def to_dot(self):
        """to dot format"""

        print "\t\"%s\" -> \"%s\" [label = \"%s/%s\", penwidth = %s];" % (
            self.v, 
            self.w,
            self._flow,
            self._capacity,
            self._capacity,
        )

    def v_from(self):
        """vertex this edge points from"""

        return self.v

    def v_to(self):
        """vertex this edge points to"""

        return self.w

    def capacity(self):
        """return capacity"""

        return self._capacity

    def flow(self):
        """return flow"""

        return self._flow

    def other(self, v_in):
        """the endpoint that's not v"""

        assert v_in in [self.v, self.w]

        if v_in == self.v:
            return self.w
        else:
            return self.v

    def residual_to(self, v_in):
        """residual capacity toward v_in"""

        assert v_in in [self.v, self.w]

        if v_in == self.w:
            return self._capacity - self._flow
        else:
            return self._flow
    
    def add_flow_to(self, v_in, delta):
        """add delta flow toward v_in"""

        assert v_in in [self.v, self.w]

        add_value = min(delta, self.residual_to(v_in))

        if v_in == self.w:
            self._flow += add_value
        else:
            self._flow -= add_value


if __name__ == "__main__":

    e1 = FlowEdge(1, 2, 4)

    print e1

    e1.add_flow_to(1, 3)

    print e1
    print e1.residual_to(1)
    print e1.residual_to(2)
