from unit import Unit
from utils import *

class Pawn(Unit):
	def __init__(self, white, pos):
		super().__init__(white, pos)
		self.starting_pos = pos
	def moves(self,board):
		moves = []
		# Move forward
		dxy = Point(0,-1) if self.white else Point(0,1)
		if board.at(self.pos+dxy) == None:
			moves.append(self.pos+dxy)
			if self.pos == self.starting_pos and board.at(self.pos+dxy*2) == None:
				moves.append(self.pos+dxy*2)
		# captures
		for check in (Point(-1,0), Point(1,0)):
			t=self.pos+dxy+check
			if t:
				if board.enPassant == t-dxy:
					moves.append(t-dxy) # en passant
				if board.at(t) and board.at(t).white != self.white:
					moves.append(t)
		return moves
	def char(self):
		return "P" if self.white else "p"
	def __str__(self):
		return super().str('p')
	def __repr__(self):
		return super().str('p')

class King(Unit):
	def __init__(self, white, pos):
		super().__init__(white, pos)
		self.moved = False
	def moves(self,board):
		moves = []
		for x in range(-1,2):
			for y in range(-1,2):
				if x or y:
					dxy=Point(x,y)
					t=self.pos+dxy
					if t and board.at(t) and board.at(t).white != self.white:
						moves.append(t)
		return moves
	def __str__(self):
		return super().str('k')
	def __repr__(self):
		return super().str('k')