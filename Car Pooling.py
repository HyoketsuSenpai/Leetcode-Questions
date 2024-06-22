class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        mx = 0
        for n in trips:
            mx = max(mx,n[2])
        mx += 1
        p = [0] * mx
        for pp,f,t in trips:
            p[f] += pp
            p[t] -= pp
        cur = 0
        for l in p:
            cur += l
            if cur > capacity:
                return False
        return True
