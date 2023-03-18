def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    output = ""
    for i in range (n):
        if i == n-1:
            print(a[i])
            output += str(a[i])
        else:
            print(a[i], end = ' ')
            output += str(a[i])

    return output
