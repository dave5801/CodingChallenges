import sys

class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        sameFrontAndBack = set()

        for card in range(len(fronts)):
            if fronts[card] == backs[card]:
                sameFrontAndBack.add(fronts[card])

        setOfAllCards = set(fronts) | set(backs)
        removedSameFrontAndBack = setOfAllCards - sameFrontAndBack
        return min(removedSameFrontAndBack, default=0)

if __name__ == '__main__':
    s = Solution()
    x = s.flipgame([1,2,4,4,7], [1,3,4,1,3])

    print(x)