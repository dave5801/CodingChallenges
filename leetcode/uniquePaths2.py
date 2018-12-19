class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        table = [[0]*m for space in range(n)]

        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            table[i][0] = 1

        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            table[0][i] = 1

        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j] == 0:
                    table[i][j] = table[i-1][j] + table[i][j-1]

        return table[-1][-1]

if __name__ == '__main__':
    s = Solution()

    grid = [[0,0,0],[0,1,0],[0,0,0]]

    x = s.uniquePathsWithObstacles(grid)
    print(x)