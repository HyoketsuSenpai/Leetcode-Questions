class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0

        while target != 1:
            if target % 2:
                ans += target % 2
                target -= target % 2
            elif target//2 and maxDoubles:
                target = target//2
                maxDoubles-=1
                ans += 1
            else:
                ans += target - 1
                target -= target - 1
        return ans
