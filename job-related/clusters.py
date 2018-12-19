'''
determine largest square of 1s in a 2d array.
'''

def largest_cluster_helper(matrix):
    '''probably use this to in addition to recurse function.'''

    for row in range(len(matrix)):

        #first row equals itself
        if row != 0 & row != len(matrix[row]):
            for column in range(len(matrix)):
                if column != 0 & column != len(matrix[column]):
                    #check upper left, up, and left
                    if matrix[row][column] != 0:
                        x = matrix[row-1][column-1]
                        y = matrix[row-1][column]
                        z = matrix[row][column-1]
                        #get min of three components and add 1
                        matrix[row][column] = min([x,y,z]) + 1
                    else:
                        #otherwise leave it alone, essentially
                       matrix[row][column] = 1

    return matrix[-1][-1]

if __name__ == '__main__':
    matrix = [[1,1,0,0],[1,1,1,1], [0,1,1,1], [0,1,1,1]]
    print(largest_cluster_helper(matrix))
    