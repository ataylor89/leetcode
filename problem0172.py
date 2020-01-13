class Solution(object):
    def trailingZeroes(self, n):
        a,b = 1,1
        num2,num5 = 0,0
        
        while 2**a <= n:
            num2 += int(n / 2**a)
            a += 1
            
        while 5**b <= n:
            num5 += int(n / 5**b)
            b += 1
            
        return min(num2, num5)
