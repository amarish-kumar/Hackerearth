for _ in xrange(int(raw_input())):
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    arr = map(bin, arr)
    brr = []
    for i in arr:
        cnt = 0
        for l in i:
            if l == "1":
                cnt += 1
        brr.append(cnt)
    brr = sorted(brr, reverse = True)
    summ = 0
    for i in xrange(0, k):
        summ += brr[i]
    print summ