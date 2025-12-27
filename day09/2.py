import sys
ps=[]
for l in sys.stdin:
  x,y=map(int,l.strip().split(','))
  ps.append([x,y])
N=len(ps)
def inter(r1z,r2z,l1z,l2z):
  if l1z>l2z: # Transform
    d=int(abs(l1z-l2z))
    l1z-=d
    l2z+=d
  if l1z<=r1z and r1z<l2z:
    return True
  if l1z<r2z and r2z<=l2z:
    return True
  return False
def intersects(r1,r2,l1,l2):
  r1x=r1[0]
  r1y=r1[1]
  r2x=r2[0]
  r2y=r2[1]
  l1x=l1[0]
  l1y=l1[1]
  l2x=l2[0]
  l2y=l2[1]
  if r2y<r1y: # Transform to NW-SE corners
    d=r1y-r2y
    r1y-=d
    r2y+=d
  if l1y==l2y: # W-E
    if l1y<=r1y:
      return False
    if r2y<=l2y:
      return False
    return inter(r1x,r2x,l1x,l2x)
  else: # N-S
    if l1x<=r1x:
      return False
    if r2x<=l2x:
      return False
    return inter(r1y,r2y,l1y,l2y)
def legal(r1,r2):
  print(r1,r2)
  for k in range(N):
    ints = intersects(ps[i],ps[j],ps[k],ps[k-1])
    if ints:
      return False
      print(False)
  return True
  print(True)
A=0
for i in range(N):
  for j in range(i+1,N):
    a=abs(ps[i][0]-ps[j][0])*abs(ps[i][1]-ps[j][1])
    if a>A and legal(ps[i],ps[j]):
      A=a
print(A) 
