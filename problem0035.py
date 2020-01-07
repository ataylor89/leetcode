class Solution(object):
    def searchInsert(self, nums, target):
        ln = len(nums)
        
        if target < nums[0]:
            return 0
        
        if target > nums[ln-1]:
            return ln
    
        for i in range(ln):
            if nums[i] == target:
                return i
            
            if nums[i] < target and target < nums[i+1]:
                return i+1
