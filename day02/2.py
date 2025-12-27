t=0
def g(p,l):
	if len(p)%l==0:
		s=p[:l]
		for j in range(l,len(p),l):
			if p[j:j+l]!=s:
				return False
		return True
def f(p):
	for l in range(1,len(p)):
		if g(p,l):
			return True
for x,y in map(lambda l: l.split('-'), input().split(',')):
	for i in range(int(x),int(y)+1):
		p=str(i)
		r=f(p)
		if r:
			t+=i
print(t)