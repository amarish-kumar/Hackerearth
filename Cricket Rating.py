n = int(raw_input())
if n == 0:
    print 0
else:
    arr = map(int, raw_input().split())
    current = arr[0]
    maxi = arr[0]
    for i in arr[1:]:
        current = max(i, current+i)
        maxi = max(current, maxi)
    print maxi