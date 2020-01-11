class Solution(object):
    def rotate(self, nums, k):
        if (len(nums) == 0):
            return None
        
        copy = list(nums)
        
        i = 0
        while i < len(nums):
            j = (i + k) % len(nums)
            nums[j] = copy[i]
            i += 1
            
        return nums
