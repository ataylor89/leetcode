class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        dn = [i for i in range(1, n+1)]
        
        for num in nums:
            dn[num-1] = -1
            
        return filter(lambda x:x>0, dn)
