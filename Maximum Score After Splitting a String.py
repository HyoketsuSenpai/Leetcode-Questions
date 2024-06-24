class Solution:
    def maxScore(self, s: str) -> int:
        z = s.count('0')
        o = len(s) - z
        score = 0
        co = o
        cz = 1
        if s[0] == '1':
            co -= 1
            cz -= 1
        score = co + cz

        for i in range(1, z + o - 1):
            if s[i] == '1':
                co -= 1
            else:
                cz += 1
            score = max(score, co + cz)
        
        return score
