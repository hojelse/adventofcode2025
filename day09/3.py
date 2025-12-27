import sys
ps=[]
for l in sys.stdin:
  x,y=map(int,l.strip().split(','))
  ps.append([x,y])
N=len(ps)

D=[]
for k in range(N):
  l0,l1,l2=ps[k-2],ps[k-1],ps[k]
  h1=l0[1]==l1[1]
  r1=l0[0]<l1[0]
  d1=l0[1]<l1[1]
  r2=l1[0]<l2[0]
  d2=l1[1]<l2[1]
  x=l1[0]
  y=l1[1]
  if h1 and r1 and d2: # right to down
    D.append([x+1,y-1])
  if h1 and r1 and not d2: # right to up
    D.append([x-1,y-1])
  if h1 and not r1 and d2: # left to down
    D.append([x+1,y+1])
  if h1 and not r1 and not d2: # left to up
    D.append([x-1,y+1])
  if not h1 and d1 and r2: # down to right
    D.append([x+1,y-1])
  if not h1 and d1 and not r2: # down to left
    D.append([x+1,y+1])
  if not h1 and not d1 and r2: # up to right 
    D.append([x-1,y-1])
  if not h1 and not d1 and not r2: # up to left
    D.append([x-1,y+1])

def inter(r1z,r2z,l1z,l2z):
  if l1z>l2z: # Transform
    d=int(abs(l1z-l2z))
    l1z-=d
    l2z+=d
  if r1z<=l1z and l1z<=r2z:
    return True
  if r1z<=l2z and l2z<=r2z:
    return True
  if l1z<r1z and r2z<l2z:
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
    if l1y<r1y:
      return False
    if r2y<l2y:
      return False
    return inter(r1x,r2x,l1x,l2x)
  else: # N-S
    if l1x<r1x:
      return False
    if r2x<l2x:
      return False
    return inter(r1y,r2y,l1y,l2y)

def legal(r1,r2):
  for k in range(len(D)):
    ints = intersects(ps[i],ps[j],D[k-1],D[k])
    if ints:
      return False
  return True

A=0
for i in range(N):
  for j in range(i+1,N):
    a=(1+abs(ps[i][0]-ps[j][0]))*(1+abs(ps[i][1]-ps[j][1]))
    l=legal(ps[i],ps[j])
    if a>A and l:
      print(ps[i],ps[j])
      A=a
print(A) 
