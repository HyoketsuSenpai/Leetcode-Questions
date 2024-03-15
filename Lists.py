if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N):
        s = input()
        if s == 'print':
            print(l)
        if s == 'sort':
            l.sort()
        if s == 'pop':
            l.pop()
        if s == 'reverse':
            l.reverse()
        l2 = s.split()
        if len(l2) == 3:
            l.insert(int(l2[1]), int(l2[2]))
        if l2[0] == 'append':
            l.append(int(l2[1]))
        if l2[0] == 'remove':
            l.remove(int(l2[1]))
