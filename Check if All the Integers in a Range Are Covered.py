class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = {x for x in range(left,right + 1)}
        
        for x in range(left,right + 1):

            for i in range(len(ranges)):
                if  ranges[i][0] <= x <= ranges[i][1]:
                    s.remove(x)
                    break

        return not len(s) 
