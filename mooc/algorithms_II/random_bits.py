import random
from bit_io import BitIO

with BitIO("out.txt", "w") as bo:
    for _ in xrange(1000):
        if random.random() > 0.5:
            bo.write_bits(1, 1)
        else:
            bo.write_bits(1, 0)


