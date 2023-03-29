def pagecount(n, p) -> int:
    if n == p:
        return 0
    if n % 2 == 0:
        n += 1
    if p % 2 == 0:
        p += 1
    return min(p//2, n//2 - p//2)