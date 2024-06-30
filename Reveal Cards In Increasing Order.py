class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        s = True
        l = [0] * len(deck)
        cnt = 0
        ind = 0
        deck.sort()
        
        while cnt < len(deck):
            if l[ind] == 0:
                if s:
                    l[ind] = deck[cnt]
                    cnt += 1
                s = not s
            ind += 1
            ind %= len(deck)
        return l
