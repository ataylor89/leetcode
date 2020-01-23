class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = None
        max2 = None
        max3 = None
        
        for i in range(0, len(nums)):
            if max1 == None:
                max1 = nums[i]
            elif nums[i] > max1:
                save = max2
                max2 = max1
                max1 = nums[i]
                max3 = save
            elif max2 == None and max1 != None and nums[i] < max1:
                max2 = nums[i]
            elif max2 != None and nums[i] > max2 and nums[i] < max1:
                max3 = max2
                max2 = nums[i]
            elif max3 == None and max2 != None and nums[i] < max2:
                max3 = nums[i]
            elif max3 != None and nums[i] > max3 and nums[i] < max2:
                max3 = nums[i]
        
        return max3 if max3 != None else max1
