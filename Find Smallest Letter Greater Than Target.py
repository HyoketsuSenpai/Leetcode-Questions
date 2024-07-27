class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)

        while l < r:
            m = (l + r)//2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        return letters[r] if r < len(letters) else letters[0]
