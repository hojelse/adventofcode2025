import sys
ps=[]
for l in sys.stdin:
  x,y=map(int,l.strip().split(','))
  ps.append([x,y])
A=0
for i in range(len(ps)):
  for j in range(i+1,len(ps)):
    x1,y1=ps[i]
    x2,y2=ps[j]
    dx=1+abs(x1-x2)
    dy=1+abs(y1-y2)
    a=dx*dy
    if a>A:
      A=a
print(A)
