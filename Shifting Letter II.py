class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = [0] * len(s)
        for st,end,di in shifts:
            l[st] += 1
            if end + 1 < len(s):
                l[end + 1] -= 1
            if di == 0:
                l[st] -= 2
                if end + 1 < len(s):
                    l[end + 1] += 2
                    
        ans = ''
        shift = 0
        for i in range(len(s)):

            shift += l[i]
            a = ord(s[i]) + shift
            while a > ord('z'):
                a -= 26
            while a < ord('a'):
                a += 26
            ans += chr(a)
        print(l)
        return ans

            
