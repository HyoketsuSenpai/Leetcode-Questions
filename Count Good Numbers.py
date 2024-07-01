class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def power(x,y):
            if y == 0:
                return 1
            h = power(x,y//2)
            h = (h*h)%mod
            if y % 2:
                h *= x

            return h

        return (power(5,(n + 1)//2) * power(4,n//2))%mod

        
