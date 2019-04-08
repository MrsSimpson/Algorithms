def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return s[m] | recursive_activity_selector(s, f, m, n)
    else:
        return 0


def greedy_activity_selector(s, f):
    n = len(s)
    k = 1
    print("Activity " + str(k))
    for m in range(1, n):
        if s[m] >= f[k]:
            #A = A | A{m}
            print("activity " + str(m + 1))
            k = m