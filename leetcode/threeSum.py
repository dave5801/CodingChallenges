

class Solution:
    def threeSum(self, nums):
        combos = []
        nums.sort()
        for first in range(len(nums)-2):
            
            if first > 0 and nums[first] == nums[first-1]:
                continue

            start = first + 1
            end = len(nums) - 1
            while start < end:
                sum_ = nums[first] + nums[start] + nums[end]

                if sum_ < 0:
                    start += 1
                elif sum_ > 0:
                    end -= 1
                else:
                    
                    combos.append([nums[first],nums[start],nums[end]])
                    
                    while start < end and nums[start] == nums[start+1]:
                        start+=1
                    while start < end and nums[end] == nums[end-1]:
                        end-=1
                    
                    start +=1
                    end -=1

        return combos

if __name__ == '__main__':
    
    s = Solution()
    #x = s.threeSum([-1,0,1,2,-1,-4])
    x = s.threeSum([1,-1,-1,0])
    print(x)
