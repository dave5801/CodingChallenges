class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = {}

        for jewel in J:
            if jewel not in jewels:
                jewels[jewel] = 1

        jewelCount = 0

        for stone in S:
            if stone in jewels:
                jewelCount += 1

        return jewelCount

if __name__ == '__main__':
    s = Solution()
    x = s.numJewelsInStones("z", "ZZ")

    print(x)