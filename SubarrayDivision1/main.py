# Description: https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem

def birthday(s, d, m):
    return sum([1 for i in range(len(s)) if sum(s[i:i+m]) == d])