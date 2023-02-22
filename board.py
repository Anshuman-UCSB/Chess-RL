from pieces import Pawn, King
from utils import *


class Board:
	def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
		self.board = []
		self.history = []
		positions,turn,castling,en_passant,move_count,half_move_count = FEN.split(' ')
		for r in positions.split('/'):
			row = []
			for c in r:
				if c.isdigit():
					row += [None]*int(c)
				else:
					if c in 'pP':
						row.append(Pawn(c.isupper(), Point(len(row), len(self.board))))
					elif c in 'kK':
						row.append(King(c.isupper(), Point(len(row), len(self.board))))
					else:
						row.append(c)
			self.board.append(row)
		self.whiteTurn = (turn == 'w')
		self.whiteCastle = [c in castling for c in 'KQ']
		self.blackCastle = [c in castling for c in 'kq']
		self.enPassant = Point(en_passant) if en_passant != '-' else None # remember to reset after another move
	def getMoves(self,point):
		if type(point) == str:
			point = Point(point)
		piece = self.at(point)
		if piece:
			return piece.moves(self)
		else:
			return []

	def at(self, point):
		if type(point) == str:
			point = Point(point)
		x,y=point
		return self.board[y][x]
	def __str__(self):
		o="  "
		for i,r in enumerate(self.board):
			o+=str(8-i)+' '
			for v in r:
				if v:
					try:
						o+=v.char()
					except:
						o+=str(v)
				else:
					o+=' '
			o+='\n  '
		o+='  abcdefgh'
		return o

if __name__ == "__main__":
	b=Board(FEN="rnbqkbnr/pppppppp/8/8/8/pppppppp/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
	print(b)
	b2=(b.at("b2"))
	print(b2.moves(b))
	print(b.getMoves("b7"))