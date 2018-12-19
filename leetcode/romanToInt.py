class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'I': 1,'V':5,'X':10,'L':50,'C': 100, 'D':500, 'M':1000}

        r = 0

        for i in range(len(s)):
            pair = s[i:i+2]

            for j in range(len(pair),-1,-1):
                if pair[j] != 'I' and pair[j-1] == 'I':
                    r += romans[[pair[j]]]
                    r -= 1
                else:
                    r += romans[[pair[j]]]

        

        return r

if __name__ == '__main__':
    s = Solution()
    x = s.romanToInt("III")
    print(x)