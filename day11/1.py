import sys
G={}
for l in sys.stdin:
  a,r=l.split(": ")
  outs=r.strip().split(" ")
  for x in outs:
    G[a]=outs
c=0
Q=[]
Q.append('you')
while len(Q)>0:
  x=Q.pop(0)
  if x=='out':
    c+=1
    continue
  for y in G[x]:
    Q.append(y)
print(c)

