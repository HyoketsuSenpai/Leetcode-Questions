class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        exp = defaultdict(int)
        ans = 0
        for n in answers:
            exp[n] += 1
            if exp[n] == n + 1:
                ans += n+1
                exp[n] = 0
        for n in exp:
            if exp[n]:
                ans += n+1
        return ans
