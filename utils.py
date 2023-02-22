def XYtoLN(x,y):
	return chr(x+ord('a'))+str(8-y)

def LNtoXY(ln):
	l,n=ln
	return ord(l)-ord('a'),8-int(n)

def shift(ln, dx, dy):
	x,y = LNtoXY(ln)
	dy*=-1
	if x+dx < 0 or x+dx > 7 or y+dy < 0 or y+dy > 7:
		return None
	return XYtoLN(x+dx, y+dy)

class Point:
	def __init__(self,*args):
		if len(args)==2:
			self.x,self.y=args
		else:
			self.x,self.y=LNtoXY(args[0])

	def __str__(self):
		return f"({self.x},{self.y})"
	def __repr__(self):
		return f"({self.x},{self.y})"
	def __add__(self,other):
		t= Point(self.x+other.x,self.y+other.y)
		if 0<=t.x<=7 and 0<=t.y<=7:
			return t
		else: return None
	def __sub__(self,other):
		t= Point(self.x-other.x,self.y-other.y)
		if 0<=t.x<=7 and 0<=t.y<=7:
			return t
		else: return None
	def __mul__(self,scalar):
		return Point(self.x*scalar,self.y*scalar)
	def __getitem__(self, i):
		if i==0: return self.x
		elif i==1: return self.y
		else: raise IndexError
	def __setitem__(self, i, v):
		if i==0: self.x=v
		elif i==1: self.y=v
		else: raise IndexError