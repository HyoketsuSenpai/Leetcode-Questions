class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = [0,0]
        for n in bills:
            if n == 20:
                if d[1]:
                    d[0] -= 1
                    d[1] -= 1
                else:
                    d[0] -= 3
            elif n == 10:
                d[0] -= 1
                d[1] += 1
            else:
                d[0] += 1
            print(*d)
            if d[0] < 0 or d[1] < 0:
                return False
        return True
