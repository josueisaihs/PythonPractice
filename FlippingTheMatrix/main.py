# https://www.hackerrank.com/challenges/flipping-the-matrix/problem

def flippingMatrix(matrix):
    n = int(len(matrix)/2)
    return sum(map(lambda i: sum(map(lambda j: max(matrix[i][j], matrix[i][(2*n-1)-j], matrix[(2*n-1)-i][j], matrix[(2*n-1)-i][(2*n-1)-j]), range(n))), range(n)))
