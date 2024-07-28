class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1

        def check(m):
            hh = 0
            for p in piles:
                hh += p//m
                if p % m:
                    hh += 1
            return hh
        while l <= r:
            m = (l + r)//2
            if check(m) > h:
                l = m + 1
            elif check(m) < h:
                r = m - 1
            elif check(m) == h:
                if m - 1 == 0 or check(m - 1) < h:
                    return m
                r = m - 1

            
        return l
