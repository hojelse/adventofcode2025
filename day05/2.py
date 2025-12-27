import sys
s=set()
for l in sys.stdin:
	l=l.strip()
	if l=="":break
	a,b=map(int,l.split('-'))
	for i in range(a,b+1):
		s.add(i)
print(len(s))