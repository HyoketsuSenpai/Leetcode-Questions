n, m = map(int,input().split())
nn = list(map(int,input().split()))
mm = list(map(int,input().split()))

i = 0
j = 0
while i < n and j < m:
    if nn[i] < mm[j]:
        i += 1
    elif nn[i] >= mm[j]:
        j += 1
        print(i, end = ' ')
while j < m:
    print(i, end = ' ')
    j += 1
