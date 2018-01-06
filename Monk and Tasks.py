
for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    brr = map(bin, arr)
    crr = []
    for i in brr:
        cnt = 0
        for k in i:
            if k == "1":
                cnt += 1
        crr.append(cnt)
    arr = zip(arr, crr)
    arr = sorted(arr, key= lambda x:(x[1],x[0]))
    print " ".join(str(i[0]) for i in arr)