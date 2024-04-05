class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = 1
        if num < 0:
            sign = -1
            num = num * -1
        
        l = list(str(num))
        
        l.sort()
        if sign == -1:
            l.reverse()
            return int("".join(l)) * sign
        
        for i in range(len(l)):
            
            if l[i] != '0':
                l[0],l[i] = l[i],l[0]
                break


                 
        print(l)
        
        return int("".join(l)) * sign
