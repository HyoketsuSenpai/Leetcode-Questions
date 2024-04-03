class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        j = len(arr2)
        arr2 = {arr2[i] : i for i in range(j)}
        arr1.sort(key=lambda x : arr2.get(x, j + x))
        return arr1
