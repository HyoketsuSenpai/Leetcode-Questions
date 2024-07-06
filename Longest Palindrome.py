class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        add = False
        ans = 0
        for cn in c:
            
            if c[cn] >= 2:
                ans += c[cn]//2
                
            if c[cn] % 2:
                add = True
        ans *= 2
        if add:
            ans += 1
        return ans
