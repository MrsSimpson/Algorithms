def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    return q


def bottom_up_cut_rod(p, n):
    r = [0 for i in range(n+1)]
    r[0] = 0
    for j in range(1, n):
        q = -1
        for i in range(j):
            q = max(q, p[i] + r[j-i-1])
        r[j] = q
    return r[n]

