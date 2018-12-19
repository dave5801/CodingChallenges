class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for firstNumber in range(len(nums)-2):
            start = firstNumber+1
            end = len(nums)-1

            while start < end:
                sum_ = nums[firstNumber] + nums[start] + nums[end]

                if sum_ == target:
                    return sum_

                if abs(sum_ - target) < abs(closestSum - target):
                    closestSum = sum_

                if sum_ < target:
                    start +=1
                if sum_ > target:
                    end -= 1
        return closestSum 

if __name__ == '__main__':
    
    s = Solution()
    #x = s.threeSum([-1,0,1,2,-1,-4])
    x = s.threeSumClosest([-1,2,1,-4], 1)
    print(x)