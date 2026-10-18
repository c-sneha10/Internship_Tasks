#Problem Name:Set .difference() Operation
#HackerRank:https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

print(len(english.difference(french)))
