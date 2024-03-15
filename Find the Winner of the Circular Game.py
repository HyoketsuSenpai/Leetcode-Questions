class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        fr = [i + 1 for i in range(n)]
        s = n
        pos = 0

        while s > 1:
             
             p = (k - 1 + pos) % s
             fr.pop(p)
             pos = p
             s -= 1
        return fr[0]
