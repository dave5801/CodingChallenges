class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = []

        for i in range(len(nums)):
            start = i+1
            end = len(nums)
            for j in range(len(nums)):
                if j != i:
                    temp = nums[start]
                    nums[start] = nums[end]
                    nums[end] = temp

                    perms.append(nums)

                    start += 1
                    end -= 1
        return perms

if __name__ == '__main__':
    s = Solution()
    x = s.permute([1,2,3])
    print(x)