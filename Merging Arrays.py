n , m = map(int, input().split())
nn = list(map(int,input().split()))
mm = list(map(int,input().split()))

i = 0
j = 0

l = list()

while i < n and j < m:
    if nn[i] < mm[j]:
        l.append(nn[i])
        i += 1
    else:
        l.append(mm[j])
        j += 1
while i < n:
    l.append(nn[i])
    i += 1
while j < m:
    l.append(mm[j])
    j += 1
print(*l)
