#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    x = 0; c = list(sorted(c))
    for i in range(0, len(c)-1):
        if (c[i+1] - c[i]) // 2 > x:
            x = (c[i+1] - c[i]) // 2
    return max(x, c[0], n-1 - c[-1])
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
