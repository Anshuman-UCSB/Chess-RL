from unit import Unit
from utils import *

class Pawn(Unit):
	def __init__(self, white, pos):
		super().__init__(white, pos)
		self.starting_pos = pos
	def moves(self,board):
		moves = []
		# Move forward
		if self.white:
			if self.pos[1] == '2' and board.at(self.pos[0] + '3') == None:
				moves.append(self.pos[0] + '4')
			if self.pos[1] != '8':
				moves.append(self.pos[0] + str(int(self.pos[1])+1))
		else:
			if self.pos[1] == '7':
				moves.append(self.pos[0] + '5')
			if self.pos[1] != '1':
				moves.append(self.pos[0] + str(int(self.pos[1])-1))
		moves = [m for m in moves if board.at(m) == None]
		
		# Capture moves
		if self.white:
			for test in (shift(self.pos, 1,1), shift(self.pos, -1,1)):
				print(test)
				if test and board.at(test) and board.at(test).white == False:
					moves.append(test)
		return moves
	def char(self):
		return "P" if self.white else "p"
	def __str__(self):
		return super().str('p')
	def __repr__(self):
		return super().str('p')