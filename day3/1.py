import sys
def next(a,b):
	c=a
	for i in range(a,b+1):
		if bs[i]>bs[c]:
			c=i
	return c
s=0
for l in sys.stdin:
	bs=list(map(int,l.strip()))
	N=2
	r=[]
	n=-1
	for j in range(N):
		n=next(n+1,len(bs)-(N-j))
		r.append(str(bs[n]))
	s+=int(''.join(r))
print(s)