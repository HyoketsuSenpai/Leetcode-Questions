# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
s1 = set(map(int,input().split()))
k= int(input())
s2 = set(map(int,input().split()))
print(len(s1 | s2))
