class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def rev(s):
            s = s[::-1]
            a = ''
            for i in range(len(s)):
                if s[i] == '1':
                    a += '0'
                else:
                    a += '1'
            return a
        def sn(n):
            if n == 1:
                return '0'
            a = sn(n-1)
            if len(a) >= k:
                return a
            return a + '1' + rev(a)
        return sn(n)[k-1]
