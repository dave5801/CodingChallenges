class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        if n == 1:
            return True

        start = 3

        while start < n:
            start *= 3

        if start == n:
            return True

        return False

if __name__ == '__main__':
    s = Solution()
    x = s.isPowerOfThree(1)
    print(x)