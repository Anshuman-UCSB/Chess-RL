from unit import Unit, Pawn

def _xyToLN(x,y):
	return chr(x+ord('a'))+str(y+1)

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
						row.append(Pawn(c.isupper(), (len(row), len(self.board))))
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
					o+=str(v)
				else:
					o+=' '
			o+='\n  '
		o+='  abcdefgh'
		return o

if __name__ == "__main__":
	b=Board()
	print(b.at("a1"))
	print(b)