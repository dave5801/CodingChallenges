class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0

        table = [0]*(n+1)
        table[1] = nums[0]

        for i in range(2, n+1):
            table[i] = max(table[i-1], nums[i-1] + table[i-2])

        return table[n]

if __name__ == '__main__':
    s = Solution()
    x = s.rob([1,2,3,1])
    print(x)