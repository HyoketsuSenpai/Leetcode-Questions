class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = []
        c = [0]*n
        cur = 0
        for f,l,s in bookings:
            c[f - 1] += s
            if l != n:
                c[l] += -s
        for i in range(n):
            cur += c[i]
            ans.append(cur)
        return ans
