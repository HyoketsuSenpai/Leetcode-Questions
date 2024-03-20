# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n,m = map(int, input().split())
d1 = defaultdict(list)
d2 = list()
for i in range(n):
    x = input()
    d1[x].append(i + 1)
for i in range(m):
    d2.append(input())
    
for x in d2:
    if x in d1:
        for i in range(len(d1[x])):
            print(d1[x][i], end = ' ')
    else:
        print(-1, end= '')
    print()
