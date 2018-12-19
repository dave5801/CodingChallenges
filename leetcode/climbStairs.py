class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n ==1:
            return n

        L = []

        for i in range(n+1):
            if i == 0 or i == 1:
                L.append(1)
            else:
                L.append(L[i-1] + L[i-2])

        return L[-1]

if __name__ == '__main__':
    s = Solution()
    x = s.climbStairs(5)
    print(x)
        