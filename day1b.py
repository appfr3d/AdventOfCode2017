import sys
from math import *

puzzle = sys.argv[1]

lst = [int(i) for i in str(puzzle)]

s = 0
jump = int(len(lst)/2)

for x in range(0,len(lst)):
	if lst[x] == lst[(x+jump)%len(lst)]:
		s = s + lst[x]

print('\n\n\n')
print(s)