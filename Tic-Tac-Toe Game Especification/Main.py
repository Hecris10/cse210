from distutils.command.clean import clean
import os
"""
    Tic-Tac-Toe Game
    Game made by Helamã Ewerton"""
    


onePos = '1'
twoPos = '2'
threePos = '3'
fourPos = '4'
fivePos = '5'
sixPos = '6'
sevenPos = '7'
eiPos = '8'
ninPos = '9'
playerOne = ''
playerTwo = ''
command = ''
playOption = ''
playerOneWon = False
playerTwoWon = False

def cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def startGame():
    print("Welcome to Tic Toe Game\n")
    playerOne = input("The player one is going to play with the X. Please, type your name\n>>>")
    print('Thank you ' + playerOne + '\n Now I want to meet the Player two')
    playerTwo = input("The player two is going to play with the O. Please, type your name\n>>>")
    print("Thank you " + playerTwo)
    print(playerOne + ' and ' + playerTwo + ' be welcomed. We are gonna start this battler')
    startGameOption()

def startGameOption():
    command = input("\nPlease press space bar and enter to start the game\n")
    
    if(command==' '):
        cleanScreen()
        main()
    else:
        print('Wrong Option!')
        startGameOption
        
def restartGame():
    onePos = '1'
    twoPos = '2'
    threePos = '3'
    fourPos = '4'
    fivePos = '5'
    sixPos = '6'
    sevenPos = '7'
    eiPos = '8'
    ninPos = '9'
    playerOne = ''
    playerTwo = ''
    command = ''
    playOption = ''
    playerOneWon = False
    playerTwoWon = False

def main():
    cleanScreen()
    drawTab()
    result = playing()
    

def playing():    
    while(playerOneWon==False and playerTwoWon==False):
        
        playerOneMatch()
        if(playerOneWon==True):
            return 1
        drawTab()
        playOption = ''
        
        PlayerTwoMatch()
        if(playerTwoWon==True):
            return 2
        drawTab()
        playOption = ''
    

        
        

def playerOneMatch():
    print("Now It's " + playerOne + "'s turn\nChoose one for the available fields\n")
    playOption = input()
    chooseField('X',playOption)

def PlayerTwoMatch():
    print("Now It's " + playerTwo + "'s turn\nChoose one for the available fields\n")
    playOption = input()
    chooseField('O',playOption)
    drawTab()
    playOption=''


def chooseField(playerSymbol, optionChosed):
    if(optionChosed=='1'):
        onePos = playerSymbol
        print('O usuario escolheu ' + optionChosed)
        print('o campo agora eh: ' + onePos)
        drawTab()
    
    elif(optionChosed=='2'):
        twoPos = playerSymbol
    elif(optionChosed=='3'):
        threePos = playerSymbol
    elif(optionChosed=='4'):
        fourPos = playerSymbol
    elif(optionChosed=='5'):
        fivePos=playerSymbol
    elif(optionChosed=='6'):
        sixPos=playerSymbol
    elif(optionChosed=='7'):
        sevenPos=playerSymbol
    elif(optionChosed=='8'):
        eiPos=playerSymbol
    elif(optionChosed=='9'):
        ninPos=playerSymbol
    else:
        print('Invalid option\nPLease try again')
        chooseField(playerSymbol, optionChosed)
    
        
    
def drawTab():
    cleanScreen()
    print('---Tic Tac Toe Game---')
    print('--------'+str(onePos)+'|'+str(twoPos)+'|'+str(threePos)+'--------')
    print('--------'+str(fourPos)+'|'+str(fivePos)+'|'+str(sixPos)+'--------')
    print('--------'+str(sevenPos)+'|'+str(eiPos)+'|'+str(ninPos)+'--------')


startGame()
