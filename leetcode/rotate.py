class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n= k % len(nums)
        while(n > 0):
            x = nums.pop()
            nums.insert(0, x)
            n -= 1
