class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        
        stack = []
        
        while i < len(nums1) and j < n:
            num1 = nums1[i]
            num2 = nums2[j]
                
            if i >= m:
                if len(stack) > 0 and stack[0] < num2:
                    nums1[i] = stack[0]
                    stack.pop(0)
                    i += 1
                else:
                    nums1[i] = num2
                    i += 1
                    j += 1
                
            else:
                if len(stack) > 0 and stack[0] < num2:
                    if stack[0] < num1:
                        nums1[i] = stack[0]
                        stack.append(num1)
                        stack.pop(0)
                    else:
                        i += 1
                else:
                    if num2 < num1:
                        nums1[i] = num2
                        stack.append(num1)
                        j += 1                    
                    i += 1
                    
                        
        while i < len(nums1) and len(stack) > 0:
            tmp = nums1[i]
            nums1[i] = stack[0]
            stack.append(tmp)
            stack.pop(0)
            i += 1
        
        return nums1
