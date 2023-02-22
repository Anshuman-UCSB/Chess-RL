class Unit:
	def __init__(self, white, pos):
		self.white = white
		self.pos = pos
	def str(self, char):
		return (char.upper() if self.white else char) + " at " + self.pos
	def moves(self,board):
		return []