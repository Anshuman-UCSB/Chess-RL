class Unit:
	def __init__(self, white, pos):
		self.white = white
		self.pos = pos
	def moves(self,board):
		return []

class Pawn(Unit):
	def __init__(self, white, pos):
		super().__init__(white, pos)
		self.starting_pos = pos
	def moves(self,board):
		x,y=self.pos
	def __str__(self):
		return "P" if self.white else "p"
	def __repr__(self):
		return "P" if self.white else "p"