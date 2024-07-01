class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        sr = 0
        sd = 0
        r = senate.count('R')
        d = len(senate) - r
        q = deque(senate)

        while r and d:
            bb = q.popleft()
            if bb == 'R' and not sr:
                
                sd += 1
                d -= 1
                q.append(bb)
            elif bb == 'R' and sr:
                sr -= 1
            elif bb == 'D' and not sd:
                
                sr += 1
                r -= 1
                q.append(bb)
            else:
                sd -= 1
        if r:
            return 'Radiant'
        return 'Dire'
            
