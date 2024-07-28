class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        if x <= 1:
            return x
        while l <= r:
            m = (l + r)//2
            if m*m < x:
                l = m + 1
            if m*m > x:
                if (m - 1) * (m - 1) < x:
                    return m - 1
                r = m -1
            if m*m == x:
                return m
    
