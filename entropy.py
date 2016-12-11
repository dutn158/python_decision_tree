from __future__ import division
import math


def entropy(p):
    if p == 1 or p == 0:
        return 0
    return -p * math.log(p, 2) - (1 - p) * math.log(1 - p, 2)
