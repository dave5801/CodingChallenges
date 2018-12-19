class Solution:
    def convert(self, s, numRows):
 
        if numRows == 1 or numRows >= len(s):
            return s

        zigZagRows = [''] * numRows
        currentColumn = 0
        changeColumn = -1

        for currentLetter in s:
            zigZagRows[currentColumn] += currentLetter
            if(currentColumn%(numRows-1) == 0):
                changeColumn *= -1
            currentColumn += changeColumn

        return ''.join(zigZagRows)

if __name__ == '__main__':
    s = Solution()
    x = s.convert("PAYPALISHIRING", 3)
    print(x)