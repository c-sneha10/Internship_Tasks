#Problem Name:Validating the Phone Number
#HackerRank:https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
T = int(input())

for _ in range(T):
    number = input()
    if re.fullmatch(r'[789]\d{9}', number):
        print("YES")
    else:
        print("NO")
