class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype
        """
        tokens.sort()
        points, maxScore = 0,0
        start, end = 0, len(tokens) - 1
        tokensRemaining = len(tokens)

        while tokensRemaining > 0:
            if P >= tokens[start]:
                points += 1
                P -= tokens[start]
                start += 1
            elif points > 0:
                points -= 1
                P += tokens[end]
                end -= 1
            if points > maxScore:
                maxScore = points

            tokensRemaining -= 1

        return maxScore

if __name__ == '__main__':
    s = Solution()
    x = s.bagOfTokensScore([100], 50)
    print(x)