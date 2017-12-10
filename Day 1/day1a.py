import sys

puzzle = sys.argv[1]

lst = [int(i) for i in str(puzzle)]

s = 0

for x in range(-1,len(lst)-1):
	if lst[x] == lst[x+1]:
		s = s + lst[x]
print('\n\n\n')
print(s)