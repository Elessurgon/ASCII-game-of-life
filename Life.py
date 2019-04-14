import random
import time
from os import system
from entities import toad
from entities import glider
from entities import glider2

def createDeadGrid(width,height):
	board = [] 
	for i in range(height):
		row = []
		for j in range(width):
			row.append(0)
		board.append(row)
	return board

def randomState(createDeadGrid,width,height):
	board = createDeadGrid(width,height)
	new_board = []
	for i,row in enumerate(board):
		line = []
		for j,cell in enumerate(row):
			if random.random() <= 0.7:
				line.append(0)
			else:
				line.append(1)
		new_board.append(line)
	return new_board
	
def PrintBoard(board):
	time.sleep(0.05)
	system('cls')
	
	for i in range(2*len(board[0])):
		print('-',end='')

	for i,row in enumerate(board):
		print('\n',end='')
		print('|',end='')
		for j,cell in enumerate(row):
			if board[i][j] == 1:
				print('#',end=' ')
			else:
				print(' ',end=' ')

		print('|',end='')

	print('\n',end='')
	for i in range(2*len(board[0])):
		print('-',end='')
	print('\n')	
	return board


def nextBoardState(board):
	new_board = []
	count=0
	height = len(board)
	width = len(board[0]) 
	for i,row in enumerate(board):
		line = []
		for j,cell in enumerate(row):
			count+=1
			total = int(board[(i-1)%height][(j-1)%width] + board[i%height][(j-1)%width] + board[(i+1)%height][(j-1)%width]
				       +board[(i-1)%height][j%width]                                    + board[(i+1)%height][j%width]
				       +board[(i-1)%height][(j+1)%width] + board[i%height][(j+1)%width] + board[(i+1)%height][(j+1)%width])
			
			if board[i][j] == 1:
				if total < 2:
					line.append(0)
				elif total == 2 or total == 3:
					line.append(1)
				elif total > 3:
					line.append(0)
			else:
				if total == 3:
					line.append(1)
				else:
					line.append(0)
		new_board.append(line)

	return new_board

def loadEntities(entity,createDeadGrid,width,height):
	loaded_thing = entity()
	dead_board = createDeadGrid(width,height)
	for x, line in enumerate(loaded_thing):
		for y,char in enumerate(line):
			dead_board[x+1][y+1] = char
	return dead_board 

def main():
	
	random_board = randomState(createDeadGrid,35,30)
	while 1:
		PrintBoard(random_board)
		new_board = nextBoardState(random_board)
		random_board = PrintBoard(new_board)

	'''
	board = loadEntities(glider,createDeadGrid,35,35)
	while 1:
		PrintBoard(board)
		new_board = nextBoardState(board)
		board = PrintBoard(new_board)
	'''
if __name__ == "__main__":
	main()


