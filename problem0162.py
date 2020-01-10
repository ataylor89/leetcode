class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):            
            if i == 0 and nums[0] > nums[1]:
                return 0
            
            if (i == len(nums) - 1) and nums[i] > nums[i-1]:
                return i
            
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
        
        return None
