ps=[]
import sys
import math
for a in sys.stdin:
  ps.append(list(map(int,a.strip().split(','))))
N=len(ps)
A=[]
for i in range(N):
  for j in range(i+1,N):
    p1=ps[i]
    p2=ps[j]
    A.append([math.dist(p1,p2),i,j])
A.sort()

# union-find
S=[[1,i] for i in range(N)]
def root(x):
  while x!=S[x][1]:
    x=S[x][1]
  return x
n=len(S)
for i in range(len(A)):
  d,a,b=A[i]
  ra=root(a)
  rb=root(b)
  if ra==rb:
    continue
  n-=1
  if n==1:
    print(ps[a][0]*ps[b][0])
    exit()
  if S[ra][0]<S[rb][0]:
    S[ra][1]=rb
    S[rb][0]+=S[ra][0]
  else:
    S[rb][1]=ra
    S[ra][0]+=S[rb][0]
