class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' in s:
            return False
        
        absences = 0
        
        for i in s:
            if i == 'A':
                absences +=1
                
        return absences < 2

if __name__ == '__main__':
    s = Solution()
    x = s.checkRecord("PAALP")
    print(x)