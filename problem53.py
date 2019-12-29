class Solution(object):
    def maxSubArray(self, nums):
        ln = len(nums)
        
        maxSum = None
        subSum = None
        
        i = 0
        
        while i < ln:
            num = nums[i]
            
            if maxSum == None:
                maxSum = num
                subSum = num
                i += 1
                continue
                
            if subSum == None:
                if num > 0:
                    subSum = num
            
            elif num > subSum + num:
                subSum = num
            
            elif num < 0 and (subSum + num < maxSum) and subSum + num < 0:
                subSum = None
                        
            else:
                subSum += num
            
            if subSum > maxSum:
                maxSum = subSum
        
            i += 1
            
        return maxSum
