class Solution(object):
    def threeSum(self, nums):
        if (len(nums)) < 3:
            return None
        
        counts = {}
        solutions = {}
        
        shorterLst = []
        
        for num in nums:
            if counts.has_key(num):
                counts[num] += 1
            else:
                counts[num] = 1
                
            if counts[num] <= 3:
                shorterLst.append(num)
                
        nums = shorterLst
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                
                if sum == 0 and nums[i] != 0 and counts.has_key(0):
                    solution = [nums[i], 0, nums[j]]
                    self.encode(solution, solutions)
                    
                elif nums[i] == 0 and nums[j] == 0:
                    if counts[0] > 2:
                        solution = [0, 0, 0]
                        self.encode(solution, solutions)
                    
                elif nums[i] == 0 and counts.has_key(-1 * nums[j]):
                    solution = [nums[i], nums[j], -1 * nums[j]]
                    self.encode(solution, solutions)
                    
                elif nums[j] == 0 and counts.has_key(-1 * nums[i]):
                    solution = [nums[i], nums[j], -1 * nums[i]]
                    self.encode(solution, solutions)
                
                elif nums[i] == -1*sum or nums[j] == -1*sum:
                    if counts[-1*sum] > 1:
                        solution = [nums[i], nums[j], -1*sum]
                        self.encode(solution, solutions)
                
                elif counts.has_key(-1*sum):                
                    solution = [nums[i], nums[j], -1 * (nums[i] + nums[j])]
                    self.encode(solution, solutions)
            
        solutionslst = []
        for key in solutions:
            solutionslst.append(self.decode(key))
            
        return solutionslst
            
    def encode(self, solution, solutions):
        solution.sort()
        
        s = ""
        
        for x in solution:
            s += str(x) + " "
        
        solutions[s] = True
    
    def decode(self, solution):
        lst = []
        
        for c in solution.split(" "):
            if len(c) > 0:
                lst.append(int(c))
        
        return lst
