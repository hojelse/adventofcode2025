import sys
G={'out':[]}
for l in sys.stdin:
  a,r=l.split(": ")
  outs=r.strip().split(" ")
  for x in outs:
    G[a]=outs

def count(s,t,B):
  T={t:1}
  c=0
  def dfs(x):
    nonlocal T
    nonlocal c
    if x==t:
      return 1
    if x in T:
      return T[x]
    if x in B:
      return 0
    Rs=[0]
    for n in G[x]:
      r = dfs(n)
      Rs.append(r)
    T[x]=sum(Rs)
    return T[x]
  return dfs(s)

print(
  count('svr', 'dac', {'fft','out'}) *
  count('dac', 'fft', {'svr','out'}) *
  count('fft', 'out', {'svr','dac'}) +
  count('svr', 'fft', {'dac','out'}) *
  count('fft', 'dac', {'svr','out'}) *
  count('dac', 'out', {'svr','fft'})
)

