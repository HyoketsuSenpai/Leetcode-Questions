# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
n = int(input())
b = True
for i in range(n):
    s = set(map(int,input().split()))
    if((not A.issuperset(s)) or len(A) <= len(s)):
        print("False")
        b = False
        break
    
if b:
    print("True")
