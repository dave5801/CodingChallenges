class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastWord = ''

        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                if lastWord != '':
                    break
            else:
                lastWord+=s[i]

        return len(lastWord)
if __name__ == '__main__':
    s = Solution()
    x = s.lengthOfLastWord("Hello World")
    print(x)