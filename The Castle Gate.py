for _ in xrange(int(raw_input())):
    n = int(raw_input())
    cnt = 0
    for i in xrange(1, n + 1):
        for j in xrange(i, n + 1):
            if i != j and i ^ j <= n:
                cnt += 1
    print cnt