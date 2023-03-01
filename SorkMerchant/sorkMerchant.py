# https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem

def sorkMerchant(n, arr):
    return sum(list(map(lambda color: arr.count(color) // 2, set(arr))))