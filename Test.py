from Life import PrintBoard
from Life import nextBoardState


initial_board = [
	[0,0,0,0,0],
	[0,0,1,1,1],
	[0,1,1,1,0],
	[0,0,0,0,0],
	[0,0,0,0,0]
		]

expected_board = [
	[0,0,0,1,0],
	[0,1,0,0,1],
	[0,1,0,0,1],
	[0,0,1,0,0],
	[0,0,0,0,0]
		]


new_board = nextBoardState(initial_board)
if new_board == expected_board:
	print("Pass")
else:
	print("It was:")
	PrintBoard(initial_board)
	print("Failed,It is:")
	print(new_board)
	PrintBoard(new_board)
	print("It should have been:")
	PrintBoard(expected_board)

input()
