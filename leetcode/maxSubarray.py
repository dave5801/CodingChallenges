class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for i in nums[1:]:
            max_ending_here = max(i, max_ending_here+i)
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


if __name__ == '__main__':
    s = Solution()
    x = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(x)