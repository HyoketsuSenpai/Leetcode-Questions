class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        l.sort(key=lambda x:x[-1])
        l = [x[:-1] for x in l]
        return ' '.join(l)
