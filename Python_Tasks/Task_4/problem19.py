# Problem 19: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
if __name__ == '__main__':
    X = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    N = int(input())

    money_earned = 0

    for _ in range(N):
        size, price = map(int, input().split())

        if shoe_sizes[size] > 0:
            money_earned += price
            shoe_sizes[size] -= 1

    print(money_earned)
