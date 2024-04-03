class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        mx = 0
        l = 0
        ans = 0
        ll = ['0' for i in range(len(flips))]

        for i in range(len(flips)):
            mx = max(mx, flips[i] - 1)
            ll[flips[i] - 1] = '1'
            while l < len(flips) and ll[l] == "1":
                l += 1
            if l >= mx:
                ans += 1
        return ans
