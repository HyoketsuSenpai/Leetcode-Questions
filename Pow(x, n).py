class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n == -1:
            return 1/x
            
        h = self.myPow(x,n//2)
        h = h*h
        if n%2:
            h *= x
        
        return h
