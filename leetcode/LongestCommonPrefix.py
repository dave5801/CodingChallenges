#I'm pretty sure this was an Amazon Problem
#https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        longestPrefix = strs[0]

        for currentIndexOfEveryWord in range(1,len(strs)):
            
            for currentIndexOfWord in range(len(longestPrefix),-1,-1):
                
                if longestPrefix[:currentIndexOfWord] == strs[currentIndexOfEveryWord][:currentIndexOfWord]:
                    longestPrefix = longestPrefix[:currentIndexOfWord]
                    break
                if currentIndexOfWord == 0:
                    longestPrefix = ''
                    break

        return longestPrefix


if __name__ == '__main__':
    
    s = Solution()
    x = s.longestCommonPrefix(["flower","flow","flight"])
    print(x)