import sys

def solve(l,bs,js):
  C=set()
  Q=[]
  Q.append((0,tuple([0]*len(js))))
  while len(Q)>0:
    d,p=Q.pop(0)
    if p==js:
      return d
    if any(a>b for a,b in zip(p, js)):
      continue
    if p in C:
      continue
    C.add(p)
    for b in bs:
      n=[a + b for a, b in zip(p, b)]
      Q.append((d+1,tuple(n)))

S=0
idx=0
for l in sys.stdin:
  a,r=l[1:].replace("}\n",'').split("] ")
  b,c=r.split(" {")
  N=len(a)

  b=[list(map(int,x[1:-1].split(','))) for x in b.split(' ')]
  bs=[]
  for y in b:
    o=['0']*N
    for i in y:
      o[i]='1'
    bs.append(tuple([int(x) for x in o]))
  js=[int(x) for x in c.split(',')]
  print(idx)
  idx+=1
  S+=solve(l,bs,tuple(js))
print(S)

