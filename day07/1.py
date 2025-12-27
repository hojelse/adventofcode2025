f=input()
N=len(f.strip())
i=f.index('S')
s=[0]*N
s[i]=1
t=0

import sys
for l in sys.stdin:
  l=l.strip()
  for idx,x in enumerate(l):
    if s[idx]==1 and x=='^':
      s[idx-1]=1
      s[idx+1]=1
      s[idx]=0
      t+=1

print(t)
