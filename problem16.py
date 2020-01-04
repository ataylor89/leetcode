class Solution(object):
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None

        self.counts = {}
        
        shorterLst = []
        
        for x in nums:
            if self.counts.has_key(x) == False:
                self.counts[x] = 1
                shorterLst.append(x)
            elif self.counts[x] < 3:
                self.counts[x] += 1
                shorterLst.append(x)
                
        nums = shorterLst
        
        self.closestSum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-1):
            numi = nums[i]
            
            for j in range(i+1, len(nums)):
                numj = nums[j]
                
                self.check(numi, numj, target)
                
                if self.closestSum == target:
                    return self.closestSum

        return self.closestSum
                
    def check(self, numi, numj, target):
        s = numi + numj
        diff = abs(target - s)
        isNegative = (target - s) < 0
        
        for i in range(diff + 1):
            diffA = diff - i
            diffB = diff + i
            
            if isNegative:
                diffA *= -1
                diffB *= -1
            
            if abs(target - self.closestSum) <= i:
                return

            if self.counts.has_key(diffA) == True:
                if numi == diffA and numj == diffA:
                    if self.counts[diffA] >= 3:
                        cs = numi + numj + diffA

                        if abs(target-cs) < abs(target-self.closestSum):
                            self.closestSum = cs

                        return

                elif numi == diffA or numj == diffA:
                    if self.counts[diffA] >= 2:
                        cs = numi + numj + diffA

                        if abs(target-cs) < abs(target-self.closestSum):
                            self.closestSum = cs

                        return

                elif numi != diffA and numj != diffA and self.counts[diffA] >= 1:
                    cs = numi + numj + diffA

                    if abs(target-cs) < abs(target-self.closestSum):
                        self.closestSum = cs

                    return
            
            if self.counts.has_key(diffB) == True:
                if numi == diffB and numj == diffB:
                    if self.counts[diffB] >= 3:
                        cs = numi + numj + diffB

                        if abs(target-cs) < abs(target-self.closestSum):
                            self.closestSum = cs

                        return

                elif numi == diffB or numj == diffB:
                    if self.counts[diffB] >= 2:
                        cs = numi + numj + diffB

                        if abs(target-cs) < abs(target-self.closestSum):
                            self.closestSum = cs

                        return

                elif numi != diffB and numj != diffB and self.counts[diffB] >= 1:
                    cs = numi + numj + diffB

                    if abs(target-cs) < abs(target-self.closestSum):
                        self.closestSum = cs

                    return
