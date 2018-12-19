class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftIndex = 0
        rightIndex = len(height)-1
        maxVolume = 0

        for i in range(len(height)-1, -1,-1):
            if height[leftIndex] < height[rightIndex]:
                maxVolume = max(height[leftIndex]*i, maxVolume)
                leftIndex+=1
            else:
                maxVolume = max(height[rightIndex]*i, maxVolume)
                rightIndex-=1

        return maxVolume
        
if __name__ == '__main__':
    s = Solution()
    x = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(x)
