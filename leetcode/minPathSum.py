class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if row == 0 and col == 0:
                    continue

                if row == 0:
                    grid[row][col] += grid[row][col-1]

                elif col == 0:
                    grid[row][col] += grid[row-1][col]

                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])

        return grid[-1][-1]

if __name__ == '__main__':
    s = Solution()

    grid = [[1,3,1],[1,5,1],[4,2,1]]

    x = s.minPathSum(grid)
    print(x)