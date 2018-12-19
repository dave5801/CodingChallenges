class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        #print(self.nums[i:j+1])
        return sum(self.nums[i:j+1])

if __name__ == '__main__':
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    x = numArray.sumRange(0,5)
    print(x)