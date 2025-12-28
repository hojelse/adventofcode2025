import sys
import re
from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, PULP_CBC_CMD

N=100
variables = {i: LpVariable(str(i), lowBound=0, cat=LpInteger) for i in range(N)}

def solve(contraints):
  prob = LpProblem("Problem", LpMinimize)

  for c,vs in constraints:
      prob += c == lpSum(vs)

  prob += lpSum(variables.values())

  prob.solve(PULP_CBC_CMD(msg=False))

  return sum(var.value() for var in variables.values())

S=0
for l in sys.stdin:
  matches = re.findall(r"\(([\d,]+)\)", l)
  buttons = [[int(x) for x in t.split(',')] for t in matches]

  matches = re.findall(r"\{([\d,]+)\}", l)
  jolts = [int(x) for x in matches[0].split(',')]

  constraints=[(j,[]) for j in jolts]

  for idx,button in enumerate(buttons):
    for l in button:
      constraints[l][1].append(variables[idx])

  S+=solve(constraints)
print(S)
