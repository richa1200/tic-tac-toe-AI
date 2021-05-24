from random import randrange

class Player(object):
	def __init__(self, symbol, isComputer):
		self.symbol = symbol
		self.isComputer = isComputer
	
	def play(self, gameBoard):
		
		if self.isComputer:
			print('\nComputer\'s Turn...')
			global count
			depth, alpha, beta, isMax = 9-count, -10, 10, True
			value, place = self.alphaBeta(gameBoard, depth, alpha, beta, isMax)
			print('Computer plays at:', place+1, '\n')
		else:
			print('\nYour Turn...')
			place = int(input('Enter a number from 1 to 9: ')) - 1
			while self.isInvalid(gameBoard, place):
				place = int(input('Enter again: ')) - 1
			print('\n')

		gameBoard[place] = self.symbol

	def alphaBeta(self, gameBoard, depth, alpha, beta, isMaxPlayer):
		value = checkIfWon(gameBoard, player)
		if value != 0:
			return value, -1
		if depth == 0:
			return value, -1
		if isMaxPlayer:
			value = -10
			listOfNumbers = list(range(9))
			while listOfNumbers:
				random = listOfNumbers.pop(randrange(len(listOfNumbers)))
				if gameBoard[random] == '_':
					gameBoard[random] = player[1].symbol
					temp_value = self.alphaBeta(gameBoard, depth-1, alpha, beta, False)[0]
					if temp_value > value:
						value = temp_value
						place = random
					alpha = max(alpha, value)
					gameBoard[random] = '_'
					if alpha >= beta:
						break
		else:
			value = 10
			listOfNumbers = list(range(9))
			while listOfNumbers:
				random = listOfNumbers.pop(randrange(len(listOfNumbers)))
				if gameBoard[random] == '_':
					gameBoard[random] = player[0].symbol
					temp_value = self.alphaBeta(gameBoard, depth-1, alpha, beta, True)[0]
					if temp_value < value:
						value = temp_value
						place = random
					beta = min(beta, value)
					gameBoard[random] = '_'
					if beta <= alpha:
						break
		return value, place

	def isInvalid(self, gameBoard, place):
		
		if place not in list(range(9)):
			print('ERROR: Invalid input. Number not from 1 to 9.')
			return True
		if gameBoard[place] != '_':
			print('ERROR: Invalid input. Place already marked.')
			return True
		
		return False

	def isSymbolX(self):
		return self.symbol == 'X'

def welcomeMessage():
	msg = '\nWelcome to the classic Tic Tac Toe game against an AI.'
	print(msg)

def initialize():
	global gameBoard, player, turn, count
	gameBoard, count = list('_'*9), 0

	if input('Do you want to play first? (y/n)  ').lower() == 'y':
		player, turn = [Player('X', False), Player('O', True)], 0
	else:
		player, turn = [Player('O', False), Player('X', True)], 1

def drawBoard(gameBoard):
	for i in range(9):
		print(gameBoard[i], '\n'*((i%3)-1), end='')
	
def displayWinMsg(whoWon):
	if whoWon == 1:
		print('\nSorry. You lose. Better luck next time.')
	elif whoWon == -1:
		print('\nCongratulations! You Win!')
	else:
		print('\nIt\'s a Draw.')

def checkIfWon(gameBoard, player):
	
	symbolToNumber, gameState = {}, [[0,0,0],[0,0,0],[0,0,0]]
	symbolToNumber['X'] = 2*player[1].isSymbolX() - 1
	symbolToNumber['O'] = 2*player[0].isSymbolX() - 1
	symbolToNumber['_'] = 0
	
	for i in range(3):
		for j in range(3):
			gameState[i][j] = symbolToNumber[gameBoard[i*3+j]] 
	
	for i in range(3):
		rowcount, colcount = 0, 0
		for j in range(3):
			rowcount += gameState[i][j]
			colcount += gameState[j][i]
		if (rowcount == -3 or colcount == -3):
			return -1
		if (rowcount == 3 or colcount == 3):
			return 1
	if gameState[1][1] == -1:
		if (gameState[0][0] == -1 and gameState[2][2] == -1) or (gameState[0][2] == -1 and gameState[2][0] == -1):
			return -1
	if gameState[1][1] == 1:
		if (gameState[0][0] == 1 and gameState[2][2] == 1) or (gameState[0][2] == 1 and gameState[2][0] == 1):
			return 1

	return 0

if __name__ == '__main__':
	welcomeMessage()
	option = 'y'
	while option == 'y':
		initialize()
		whoWon = False
		while not whoWon:
			drawBoard(gameBoard)
			player[turn].play(gameBoard)
			whoWon = checkIfWon(gameBoard, player)
			turn = 1 - turn
			count += 1
			if count == 9:
				break
		drawBoard(gameBoard)
		displayWinMsg(whoWon)
		option = input('\nDo you want to play again? (y/n)\n').lower()