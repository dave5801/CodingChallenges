class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        peakSoFar = nums[0]

        for i in range(1,len(nums)):
            if i == len(nums) -1 and nums[i] > peakSoFar:
                return i

            if peakSoFar < nums[i] and nums[i] > nums[i+1]:
                return i

            peakSoFar = nums[i]
        
        return 0

if __name__ == '__main__':
    s = Solution()
    x = s.findPeakElement([2,1])
    print(x)