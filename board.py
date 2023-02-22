from pieces import Pawn
from utils import *


class Board:
	def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
		self.board = []
		for r in FEN.split('/'):
			row = []
			for c in r:
				if c.isdigit():
					row += [None]*int(c)
				else:
					if c in 'pP':
						row.append(Pawn(c.isupper(), XYtoLN(len(row), len(self.board))))
					else:
						row.append(c)
			self.board.append(row)
	def at(self, square):
		l,n=square
		n=int(n)
		l=l.lower()
		return self.board[8-n][ord(l)-ord('a')]
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
	b=Board(FEN="rnbqkbnr/pppppppp/8/8/8/pppppppp/PPPPPPPP/RNBQKBNR")
	print(b.at("a2"))
	print(b.at("a2").moves(b))
	print(b.at("h8"))
	print(b)