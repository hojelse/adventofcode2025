import sys
x=50
c=0
for line in sys.stdin:
	if line.startswith('R'):
		x+=int(line.strip().split('R')[1])
	if line.startswith('L'):
		x-=int(line.strip().split('L')[1])
	x=x%100
	if x == 0:
		c+=1
print(c)
