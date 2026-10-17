#Problem Name:Word Order
#HackerRank Link:https://www.hackerrank.com/challenges/word-order/problem
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    words = [input().strip() for _ in range(n)]

    counts = Counter(words)

    print(len(counts))
    print(*counts.values())
