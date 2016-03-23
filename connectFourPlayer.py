from TheBoardClass import *

class Player():
    def __init__(self, ox):

        self.ox = ox

    def play(self, board):

        ox = self.ox
        W = board.width

        if ox == 'X':
            player = 'X'
            other = 'O'
        else:
            player = 'O'
            other = 'X'

        print 'player: ',player

        colScore = [' ']*(W)

        for col in range(W):

            board.addMove(col,player)
            print board
            if board.allowsMove(col) == False:
                colScore[col] = -1
            elif board.winsFor(player) == True:
                colScore[col] = 100
            elif board.winsFor(other) == True:
                colScore[col] = 0
            elif board.winsFor(player) == False and board.winsFor(other) == False:
                colScore[col] = 50
            board.delMove(col)


            board.addMove(col,other)
            if board.winsFor(other) == True:
                colScore[col] = 75
            elif board.winsFor(other) == False:
                colScore[col] = 50
            board.delMove(col)

        max_value = max(colScore)
        max_index = colScore.index(max_value)

        return max_index

def hostGame():

    b = Board(7,6)
    computer = Player('X')
    print b

    while True:
        oCol = -1
        while b.allowsMove(oCol) == False:
            print '\n'
            oCol = input("O, Choose a column: ")
            print '\n'
        b.addMove(oCol,'O')
        print b
        oCol = -1


        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('O') == True:
            print 'O won!'
            return

        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('X') == True:
            print 'X won!'
            return



        xCol = -1
        while b.allowsMove(xCol) == False:
            print '\n'
            xCol = computer.play(b)
            print "Computer chose column: ",xCol
            print '\n'
        b.addMove(xCol,'X')
        print b

        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('O') == True:
            print 'O won!'
            return

        if b.isFull() == True:
            print "Truce"
            return
        elif b.winsFor('X') == True:
            print 'X won!'
            return


hostGame()