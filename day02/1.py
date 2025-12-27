s=0
for x,y in map(lambda l: l.split('-'), input().split(',')):
	for i in range(int(x),int(y)):
		p=str(i)
		l=len(p)//2
		if len(p)%2==0:
			a,b=p[:l],p[l:]
			if a==b:
				s+=i
print(s)