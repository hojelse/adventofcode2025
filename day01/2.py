import sys
x=50
c=0
for line in sys.stdin:
	y = x
	if line.startswith('R'):
		x+=int(line.strip().split('R')[1])
		while x > 99:
			c+=1
			x-=100
	if line.startswith('L'):
		x-=int(line.strip().split('L')[1])
		if y == 0 and x < 0:
			c-=1
		while x < 0:
			c+=1
			x+=100
		if x == 0:
			c+=1
	print(x, c)
print(c)