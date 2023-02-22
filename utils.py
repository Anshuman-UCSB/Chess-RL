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