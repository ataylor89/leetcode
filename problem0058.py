class Solution(object):
    def lengthOfLastWord(self, s):
        if s.isspace() or len(s) == 0:
            return 0
        
        ls = len(s)
        processingWord = False
        startIndexOfLastWord = 0
        endIndexOfLastWord = 0
        
        for i in range(ls):
            letter = str(s[i])
            
            if letter.isalpha() and processingWord == False:
                processingWord = True
                startIndexOfLastWord = i
                endIndexOfLastWord = i
               
            elif letter.isspace() and processingWord == True:
                processingWord = False
                endIndexOfLastWord = i - 1
                
            elif (i == ls - 1) and processingWord == True:
                endIndexOfLastWord = i
        

        return endIndexOfLastWord - startIndexOfLastWord + 1
