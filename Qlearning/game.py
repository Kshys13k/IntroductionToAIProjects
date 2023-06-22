import copy
import os
import random

EMPTY_BOARD=[[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "]
]

class Square:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class GameState:
    def __init__(self):
        self.board = copy.deepcopy(EMPTY_BOARD)
        self.player=Square(0,0)
        self.target=Square(0,9)

        self.board[self.player.x][self.player.y]="P"
        self.board[self.target.x][self.target.y] = "T"

    def moveUp(self):
        if self.player.x==0:
            return False
        else:
            self.board[self.player.x][self.player.y] = " "
            self.player.x-=1
            self.board[self.player.x][self.player.y] = "P"
            return True
    def moveDown(self):
        if self.player.x==9:
            return False
        else:
            self.board[self.player.x][self.player.y] = " "
            self.player.x+=1
            self.board[self.player.x][self.player.y] = "P"
            return True
    def moveLeft(self):
        if self.player.y==0:
            return False
        else:
            self.board[self.player.x][self.player.y] = " "
            self.player.y-=1
            self.board[self.player.x][self.player.y] = "P"
            return True
    def moveRight(self):
        if self.player.y==9:
            return False
        else:
            self.board[self.player.x][self.player.y] = " "
            self.player.y+=1
            self.board[self.player.x][self.player.y] = "P"
            return True
    def youWon(self):
        if self.player.x==self.target.x and self.player.y==self.target.y:
            return True
        else:
            return False
    def printBoard(self):
        for i in range (len(self.board)):
            print(self.board[i])

def win():
    os.system("clear")
    print("You Won!")


def main():
    gameState=GameState()
    gameState.printBoard()

    while 1==1:
        key=input()
        os.system("clear")

        #controling player action
        if key == "w":
            gameState.moveUp()
        elif key == "a":
            gameState.moveLeft()
        elif key == "s":
            gameState.moveDown()
        elif key == "d":
            gameState.moveRight()
        elif key == "r":
            gameState=GameState()

        gameState.printBoard()

        if gameState.youWon():
            win()
            gameState=GameState()




if __name__ == "__main__":
    main()
