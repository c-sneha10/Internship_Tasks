# Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem
import math
import os
import random
import re
import sys
def pangrams(s):
    s = s.lower()

    if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s)):
        return "pangram"
    else:
        return "not pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
