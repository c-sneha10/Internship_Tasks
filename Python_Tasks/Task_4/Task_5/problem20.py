#Problem Name:Piling Up!
#HackerRank Link:https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

def can_stack(blocks):
    blocks = deque(blocks)
    top = float('inf')

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > top:
            return "No"

        top = current

    return "Yes"


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        blocks = list(map(int, input().split()))
        print(can_stack(blocks))
