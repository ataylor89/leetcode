class Solution(object):
    def majorityElement(self, nums):
        self.counts = {}
        
        for n in nums:
            if self.counts.has_key(n) == False:
                self.counts[n] = 1
            else:
                self.counts[n] += 1
                
            if self.counts[n] > len(nums) / 2:
                return n
        
        return None
