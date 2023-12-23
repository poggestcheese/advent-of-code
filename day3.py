import sys
import re
from collections import defaultdict
filey = open("day3.txt", "r").read()
lines = filey.split('\n')
chararr = [[c for c in line] for line in lines]
chars = len(chararr)
chary = len(chararr[0])

part1 = 0
nums = defaultdict(list)
for r in range(len(chararr)):
  gears = set()
  n = 0
  has_part = False
  for c in range(len(chararr[r])+1):
    if c<chary and chararr[r][c].isdigit():
      n = n*10+int(chararr[r][c])
      for charac in [-1,0,1]:
        for symb in [-1,0,1]:
          if 0<=r+charac<chars and 0<=c+symb<chary:
            ch = chararr[r+charac][c+symb]
            if not ch.isdigit() and ch != '.':
              has_part = True
            if ch=='*':
              gears.add((r+charac, c+symb))
    elif n>0:
      for gear in gears:
        nums[gear].append(n)
      if has_part:
        part1 += n
      n = 0
      has_part = False
      gears = set()

print(part1)
part2 = 0
for k,v in nums.items():
  if len(v)==2:
    part2 += v[0]*v[1]
print(part2)
