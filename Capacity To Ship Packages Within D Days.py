class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        def check(cap):
            cnt = 0
            sm = 0
            i = 0
            while i < len(weights):
                cnt += 1
                t = cap
                while i < len(weights) and t >= weights[i]:
                    t -= weights[i]
                    i += 1
            return cnt

        while l <= r:
            m = (l + r)//2
            if check(m) == days and check(m-1) < days:
                return m
            if check(m) <= days:
                r = m - 1
            elif check(m) > days:
                l = m + 1
            if r - l<= 1:
                if check(l) <= days:
                    return l 
            
        return r
