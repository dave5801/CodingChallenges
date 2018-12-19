class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedRankings = sorted(nums, reverse = True)
        rankings = {}

        for index, number in enumerate(sortedRankings):
            if number in rankings:
                rankings[number] = None
            else:
                rankings[number] = [index]

        result = []

        for number in nums:
            if rankings[number][0] > 2:
                result.append(str(rankings[number][0] + 1))
            elif rankings[number][0] == 0:
                result.append("Gold Medal")
            elif rankings[number][0] == 1:
                result.append("Silver Medal")
            elif rankings[number][0] == 2:
                result.append("Bronze Medal")

                rankings[number].pop(0)   

        return result
        

if __name__ == '__main__':
    s = Solution()
    x = s.findRelativeRanks([10,3,8,9,4])
    print(x)