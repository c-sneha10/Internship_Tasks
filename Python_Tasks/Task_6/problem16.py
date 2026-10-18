#Problem Name:Check Subset
#HackerRank:https://www.hackerrank.com/challenges/py-check-subset/problem
T = int(input())

for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))

    m = int(input())
    B = set(map(int, input().split()))

    print(A.issubset(B))
