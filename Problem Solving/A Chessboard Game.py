#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chessboardGame' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#

def chessboardGame(x, y):
    # Write your code here
    return "Second "if 0 < x % 4 < 3 and 0 < y % 4 < 3 else "First"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()
