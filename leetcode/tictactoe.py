
class TicTacToe:
    
    def __init__(self):
        self.gameBoard = []


    def makeBoard(self):

        for i in range(3):
            #row = ["-"+ "|" + "-" + "|" + "-"]
            row = ["-", "-", "-"]
            self.gameBoard.append(row)

    def makeMove(self, playerMark, moveX, moveY):

        if self.checkIfValidMove(moveX,moveY) == True:
            #do stuff
            self.gameBoard[moveX][moveY] == playerMark
        else:
            return "not valid move"


    def checkIfValidMove(self,x,y):
        if self.gameBoard[x][y] == 'O' or self.gameBoard[x][y] == 'X':
            return False
        else:
            return True

    def updateBoard(self):
        for i in range(len(self.gameBoard)):
            for j in range(len(self.gameBoard[i])):
                print(self.gameBoard[i][j])

if __name__ == '__main__':
    t = TicTacToe()
    t.makeBoard()
    t.updateBoard()
    #t.makeMove('X', 1, 1)
    #t.updateBoard()