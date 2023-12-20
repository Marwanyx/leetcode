#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getScoreDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numSeq as parameter.
#

def getScoreDifference(numSeq):
    # Write your code here
    user1Score = 0
    user2Score = 0
    turn = 1
    while len(numSeq) != 0:
        score = numSeq.pop(0)
        if score % 2 == 0:
            numSeq.reverse()
        if turn == 1:
            user1Score = user1Score + score
            turn = 2
        else:
            user2Score = user2Score + score
            turn = 1
    return user1Score - user2Score


if __name__ == '__main__':
    s = getScoreDifference([3, 6, 2, 3, 5])
    print(s)
