class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        m = -1
        pivot = False
        ad = True
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                ad = False

        if ad:
            return False
            
        ad = True
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                ad = False

        if ad:
            return False

        for i,n in enumerate(arr):
            
            if m == n:
                return False

            if m > n and  not pivot:
                pivot = True 
            elif pivot and n > m:
                return False

            m = n
        return pivot
