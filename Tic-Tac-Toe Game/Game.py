from distutils.command.clean import clean
import os
from pickletools import optimize
from turtle import position

"""
    Tic-Tac-Toe Game
    Game made by Helamã Ewerton"""

class TicTacToe:
    def __init__(self):
        self.onePos = '1'
        self.twoPos = '2'
        self.threePos = '3'
        self.forPos = '4'
        self.fivePos = '5'
        self.sixPos = '6'
        self.sevenPos = '7'
        self.eightPos = '8'
        self.ninePos = '9'
        self.playerOneName = ''
        self.playerTwoName = ''
        self.command = ''
        self.play1Win = False
        self.play2Win = False
        self.optionsChosen = []
        self.aTie = ''
    
    def main(self):
        print('Welcome to the Tic-Tac-Toe Challenge Ultimate Game')
        print("Select One of the options below:")
        print('1 - Start Game')
        print('2 - Exit')
        option = input("\n")
         
        if(option=='1'):
             self.startGame()
             return self.main()
         
        elif(option=='2'):
            return
        else:
            print('Invalid Option. Please Try Again')
            self.main()
        
    def subMenu(self):
        print("Select One of the options below:")
        print('1 - Restart Game')
        print('2 - Exit')
        
        option = input("\n")
        
        if(option=='1'):
            self.restartGame()
            self.startGame()
            return
        elif(optimize=='2'):
            return
                    
        
    def startGame(self):
        self.cleanScreen()
        print("Let's start this match!!!")
        print("Player One, You're gonna use the X")
        self.playerOneName = input("Now, Tell me your name\n")
        print("Player Two, You're gonna use the O")
        self.playerTwoName = input("Now, Tell me your name\n")
        print(self.playerOneName + ' and ' + self.playerTwoName + ', be welcome')
        self.startGameOption()
        self.cleanScreen()
        self.gamePlay()
            

    def startGameOption(self):
        self.command = ''
        self.command = input("Press Enter to Start\n")
    
        if(self.command!=''):
            print('Invalid Option, please try again')
            return self.startGameOption()
        return    
    
    def cleanScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def drawnGame(self):
        print('++++++++ ' + self.playerOneName + ' X ' + self.playerTwoName + ' ++++++++')
        print("=======================")
     
        print('      ' + self.onePos + ' |  ' + self.twoPos + '  | ' + self.threePos + '             ')
        print('     ---  ---  ---')
        print('      ' + self.forPos + ' |  ' + self.fivePos + '  | ' + self.sixPos + '             ')
        print('     ---  ---  ---')
        print('      ' + self.sevenPos + ' |  ' + self.eightPos + '  | ' + self.ninePos + '             ')
    
    def gamePlay(self):
        self.cleanScreen()
        self.isATie()
      
        print("Player 1 Turn")
        self.drawnGame()
        print('Please select One of the available positions')
        self.playMove('X', self.playerOneName)
        self.cleanScreen()
        self.drawnGame()
        self.play1Win = self.ifWins('X')
        if(self.play1Win==True):
            
            print("Congratulations " + self.playerOneName + ".You Won this battle")
            return self.subMenu()
        
        self.isATie()
        self.cleanScreen()
        print("Player 2 Turn")
        self.drawnGame()
        print(self.playerTwoName+ " It's your turn")
        print('Please select One of the available positions')
        self.playMove('O', self.playerOneName)
        self.cleanScreen()
        self.drawnGame()
        self.play2Win = self.ifWins('O')
        if(self.play2Win==True):
            print("Congratulations " + self.playerTwoName + ".You Won this battle")
            return self.subMenu()
        
       
        return self.gamePlay()   
        
    def playMove(self, play, PlayerName):
        position = input("Position: ")
        if(position in self.optionsChosen):
            print("Unavailable Option. Please Try again")
            return self.playMove(play, PlayerName)
            
        if(position=='1'):
            self.onePos =  play
            self.optionsChosen.append(position)
            return
        elif(position=='2'):
            self.twoPos = play
            self.optionsChosen.append(position)
            return
        elif(position=='3'):
            self.threePos = play
            self.optionsChosen.append(position)
            return
        elif(position=='4'):
            self.forPos = play
            self.optionsChosen.append(position)
            return
        elif(position=='5'):
            self.fivePos= play
            self.optionsChosen.append(position)
            return
        elif(position=='6'):
            self.sixPos=play
            self.optionsChosen.append(position)
            return
        elif(position=='7'):
            self.sevenPos=play
            self.optionsChosen.append(position)
            return
        elif(position=='8'):
            self.eightPos=play
            self.optionsChosen.append(position)
            return
        elif(position=='9'):
            self.ninePos=play
            self.optionsChosen.append(position)
            return
        else:
            print('Invalid Option.' + PlayerName + ' Please select one of the numbers of available positions')
            return self.playMove(play, PlayerName)
    
    

    
    def ifWins(self, sym):
        if(self.onePos==sym and self.twoPos==sym and self.threePos==sym):
            return True
        elif(self.onePos==sym and self.forPos==sym and self.sevenPos==sym):
            return 
        elif(self.sevenPos==sym and self.eightPos==sym and self.ninePos==sym):
            playerWin = True
        elif(self.threePos==sym and self.sixPos==sym and self.ninePos==sym):
            return True
        elif(self.forPos==sym and self.fivePos==sym and self.sixPos==sym):
            return True
        elif(self.twoPos==sym and self.fivePos==sym and self.eightPos==sym):
            return True
        elif(self.onePos==sym and self.fivePos==sym and self.ninePos==sym):
            return True
        elif(self.threePos==sym and self.fivePos==sym and self.sevenPos==sym):
            return True
        
        return False
        
    def isATie(self):
        if(len(self.optionsChosen)==9):
            self.aTie = True
            print("IT'S A TIIIIIEE")
            self.subMenu()
    
    def restartGame(self):
        self.onePos = '1'
        self.twoPos = '2'
        self.threePos = '3'
        self.forPos = '4'
        self.fivePos = '5'
        self.sixPos = '6'
        self.sevenPos = '7'
        self.eightPos = '8'
        self.ninePos = '9'
        self.playerOneName = ''
        self.playerTwoName = ''
        self.command = ''
        self.play1Win = False
        self.play2Win = False
        self.optionsChosen = []
        self.aTie = ''