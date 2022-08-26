'''for problem i'''
def trickyGame(rounds, playerOne, playerTwo):
    '''converting all inputs to a useful form'''
    rounds = int(rounds)
    playerOne = playerOne.split()
    
    playerTwo = playerTwo.split()
    
    '''scores'''
    playerOneScore = 0
    playerTwoScore = 0
    for i in range(len(playerOne)):
        if evaluateScores(playerOne[i], playerTwo[i]) == "Player One":
            playerOneScore = playerOneScore + 1
        elif evaluateScores(playerOne[i], playerTwo[i]) == "Player Two":
            playerTwoScore = playerTwoScore + 1
        else:
            playerOneScore = playerOneScore
    if playerOneScore > playerTwoScore:
        print("PLAYER 1 WINS")
    elif playerTwoScore > playerOneScore:
        print("PLAYER 2 WINS")
    else:
        print("TIE")

def evaluateScores(playerOneCard, playerTwoCard):
    score1 = findPointValue(playerOneCard)
    score2 = findPointValue(playerTwoCard)
    if score1 > score2:
        
        return("Player One")
    elif score1 == score2:
        
        return("Tie")
    else:
        
        return("Player Two")
    

def findPointValue(card):
    if card == "J":
        pointValue = 10
    elif card == "Q":
        pointValue = 11
    elif card == "K":
        pointValue = 12
    elif card == "A":
        pointValue = 13
    else:
        card = int(card)
        
        pointValue = card
    
    return(pointValue)

'''trickyGame("5", "A 3 2 Q 7", "5 7 2 K 4")'''

'''for problem j'''
'''remember to ask the question about multi-line inputs'''
def queens(inputString):
    inputString = inputString.splitlines()
    '''extracting board dimension and casting it as an integer'''
    boardDimension = inputString[0]
    boardDimension = int(boardDimension)
    inputString.pop(0)
    '''splitting the remaining lines, casting their elements as integers, and adding them to a new array'''
    coordinatesArray = []
    for i in range(len(inputString)):
        currentCoord = inputString[i].split()
        currentCoord = [int(k) for k in currentCoord]
        coordinatesArray.append(currentCoord)
        print(coordinatesArray)
    '''declaring variables that represent if two queens are in the same row, column, or diagonal (defaults to false)'''
    queensRow = False
    queensColumn = False
    queensDiagonal = False
    '''checking if any queens are in same column by comparing set of x to list of x'''
    xCoords = []
    for i in range(boardDimension):
        currentCoord = coordinatesArray[i]
        x = currentCoord[0]
        xCoords.append(x)
    if len(xCoords) != len(set(xCoords)):
        queensColumn = True
    else:
        queensColumn = False
    '''checking if any queens are in same row by comparing set of y to list of y'''
    yCoords = []
    for i in range(boardDimension):
        currentCoord = coordinatesArray[i]
        y = currentCoord[1]
        yCoords.append(y)
    if len(yCoords) != len(set(yCoords)):
        queensRow = True
    else:
        queensRow = False
    '''checking if queens are on same diagonal'''
    for i in range(boardDimension):
        currentCoord = coordinatesArray[i]
        x = currentCoord[0]
        y = currentCoord[1]
        for item in coordinatesArray:
            newX = item[0]
            newY = item[1]
            if item == currentCoord:
                queensDiagonal = queensDiagonal
            elif x - y == newX - newY or x + y == newX + newY:
                queensDiagonal = True
            else:
                queensDiagonal = queensDiagonal
    '''returning overall results'''
    if queensRow == queensColumn == queensDiagonal == False:
        print("CORRECT")
    else:
        print("INCORRECT")
                


queens('''8
1 5
6 2
3 1
5 0
4 6
0 3
2 7
7 4''')
    
