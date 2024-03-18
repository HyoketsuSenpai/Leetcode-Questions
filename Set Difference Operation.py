# Enter your code here. Read input from STDIN. Print output to STDOUT
e = int(input())
s1 = set(map(int,input().split()))
f = int(input())
s2 = set(map(int,input().split()))
print(len(s1.difference(s2)))
