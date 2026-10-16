#Problem Name : Find the Runner-Up Score!
#HackerRank Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = sorted(set(arr))
    print(unique_scores[-2])
