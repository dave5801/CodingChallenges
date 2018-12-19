class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <=1:
            return 0

        min_ = prices[0]
        max_ = 0

        for i in prices[1:]:
            max_ = max(max_, i - min_)
            min_ = min(min_, i)

        return max_

if __name__ == '__main__':
    s = Solution()
    x = s.maxProfit([7,1,5,3,6,4])
    print(x)