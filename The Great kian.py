n = int(raw_input())
arr = map(int,raw_input().split())
l,m,p = 0,1,2
summ = 0
for i in xrange(l,n,3):
    summ += arr[i]
print summ,
summ = 0
for i in xrange(m,n,3):
    summ += arr[i]
print summ,
summ = 0
for i in xrange(p,n,3):
    summ += arr[i]
print summ    