for _ in xrange(int(raw_input())):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    cnt1, cnt2 = 0,0
    for i in arr:
        if i % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    print cnt1 * cnt2