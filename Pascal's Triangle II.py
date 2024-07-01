class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1,1]
        if rowIndex == 0:
            return [1]
        l = [0] + self.getRow(rowIndex - 1)+ [0]
        r = []
        for i in range(len(l) - 1):
            r.append(l[i] + l[i + 1])
        return r
