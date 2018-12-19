class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        #sum1 = matrix[]
        s = 0
        for row in range(row1, row2+1):
            s += sum(matrix[row][col1:col2+1])
        return s

if __name__ == '__main__':

    matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],[1, 2, 0, 1, 5],[4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]]

    numMatrix = NumMatrix(matrix)
    x = numMatrix.sumRegion(2, 1, 4, 3)
    print(x)