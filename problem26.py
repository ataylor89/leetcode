class Solution(object):
    def removeDuplicates(self, nums):
        for i in range(len(nums)):
            if i == len(nums) - 1:
                break
            
            j = i + 1
            
            while j < len(nums) and nums[i] == nums[j]:
                nums.pop(j)
                
        return len(nums)
