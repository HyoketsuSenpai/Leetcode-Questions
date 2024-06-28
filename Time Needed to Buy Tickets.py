class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        d = deque(tickets)
        t = 0
        s = len(tickets)
        while d:
            t+=1
            d[0]-=1
            n = d.popleft()
            if n == 0:
                if k == 0:
                    return t
                s-=1
            else:
                d.append(n)

            k-=1
            if k < 0:
                k = s - 1
