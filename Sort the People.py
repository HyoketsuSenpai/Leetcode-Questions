class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [[heights[i],names[i]] for i in range(len(names))]
        l.sort(reverse=True)
        #print(l)
        return [name[1] for name in l]
