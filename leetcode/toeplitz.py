class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        '''
        '''
        for col in range(len(matrix) - 1):
            for row in range(len(matrix[0])-1):
                if matrix[col][row] != matrix[col+1][row+1]:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()

    matrix = [
    [1,2,3,4],
    [5,3,2,3],
    [9,5,1,2]
    ]

    x = s.isToeplitzMatrix(matrix)
    print(x)