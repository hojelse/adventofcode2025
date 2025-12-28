import sys

def solve(l,bs,js):
  C=set()
  Q=[]
  Q.append((0,int(b'0',2)))
  while len(Q)>0:
    d,p=Q.pop(0)
    if p==l:
      return d
    if p in C:
      continue
    C.add(p)
    for b in bs:
      Q.append((d+1,p^b))

S=0
for l in sys.stdin:
  a,r=l[1:].replace("}\n",'').split("] ")
  b,c=r.split(" {")
  N=len(a)

  l=int(''.join(['1' if x=='#' else '0' for x in a]),2)
  b=[list(map(int,x[1:-1].split(','))) for x in b.split(' ')]
  bs=[]
  for y in b:
    o=['0']*N
    for i in y:
      o[i]='1'
    bs.append(int(''.join(o),2))
  js=c
  S+=solve(l,bs,js)
print(S)

