from TheBoardClass import *

import random

class Player():
    """ an AI player for Connect Four """
    def __init__(self, ox, tiebreaker, numberOfPlays):
        """ the constructor """
        self.ox = ox
        self.tbt = tiebreaker
        self.np = numberOfPlays

    def __repr__( self ):
        """ creates an appropriate string """
        s = "Player for " + self.ox + "\n"
        s += "  with tiebreak type: " + self.tbt + "\n"
        s += "  and number of plays == " + str(self.np) + "\n\n"
        return s

    def oppCh(self):
        if self.ox == 'X':
            return 'O'
        elif self.ox == 'O':
            return 'X'

    def scoreBoard(self, b):
        """
        This should return 100.0 if the board b is a win for self. It should return 50.0 if it is neither a win nor a loss for self,
        and it should return 0.0 if it is a loss for self (i.e., the opponent won)
        """
        if b.winsFor(self.ox) == True:
            return 100
        elif b.winsFor(self.oppCh()) == True:
            return 0
        else:
            return 50

    def tieBreakMove(self, scores):
        """input score: a list of scores"""
        max_index = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_index.append(i)

        if len(max_index) > 1:
            if self.tbt == 'LEFT':
                max_index0 = max_index[0]
            elif self.tbt == 'RIGHT':
                max_index0 = max_index[-1]
            elif self.tbt == 'RANDOM':
                max_index[random.randint(range(len(max_index)))]
        else:
            max_index0 = max_index


        return max_index0

    def scoresFor(self, b):

        self.scores = [50]*b.width

        counter

        for col in range(b.width):
            if b.allowsMove == False:
                self.scores[col] = -1
            elif b.winsFor(self.ox):
                self.scores[col] = 100
            elif self.np == 0:
                self.scores[col] = 50
            elif self.np > 0 and counter <= self.np:
                print counter
                b.addMove(col,self.ox)
                if b.winsFor(self.ox) == True:
                    self.scores[col] = 100
                else:
                    opponent = Player(self.oppCh, self.tbt, self.np)
                    opponent.scoresFor(b)

            if opponent.scores[col] == 100:
                self.scores[col] = 0
            else:
                self.scores[col] = opponent.scores[col]



        return self.scores

b = Board(7,6)
b.setBoard( '1211244445' )
print b

print Player('X', 'LEFT', 1).scoresFor(b)

"""
scores = [0, 0, 50, 0, 50, 50, 0]
p = Player('X', 'LEFT', 1)
p2 = Player('X', 'RIGHT', 1)
print p.tieBreakMove(scores)
print p2.tieBreakMove(scores)

b = Board(7,6)
b.setBoard( '01020305' )
print b

p = Player( 'X', 'LEFT', 0 )
print p.scoreBoard(b)
print Player('O', 'LEFT', 0).scoreBoard(b)
print Player('O', 'LEFT', 0).scoreBoard( Board(7,6) )


class Player1():
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
"""