f=input()
N=len(f.strip())
i=f.index('S')
s=[0]*N
s[i]=1

import sys
for l in sys.stdin:
  l=l.strip()
  for idx,x in enumerate(l):
    if s[idx]>=1 and x=='^':
      s[idx-1]+=s[idx]
      s[idx+1]+=s[idx]
      s[idx]=0

print(sum(s))
