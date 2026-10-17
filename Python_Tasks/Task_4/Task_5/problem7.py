#Problem Name:Symmetric Difference
#HackerRank Link:https://www.hackerrank.com/challenges/symmetric-difference/problem
if __name__ == '__main__':
    M = int(input())
    a = set(map(int, input().split()))

    N = int(input())
    b = set(map(int, input().split()))

    result = sorted(a.symmetric_difference(b))

    for num in result:
        print(num)
