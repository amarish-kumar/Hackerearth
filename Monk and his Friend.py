for _ in xrange(int(raw_input())):
    a, b = map(int, raw_input().split())
    l = bin(b ^ a)
    cnt = 0
    for i in l:
        if i == "1":
            cnt += 1
    print cnt