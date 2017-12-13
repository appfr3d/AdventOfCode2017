puzzle = open("day5Input.txt", "r")
l = []
for line in puzzle:
	l.append(int(line))

i = 0
steps = 0
while i < len(l):
	steps = steps + 1
	val = l[i]
	if val >= 3:
		l[i] = l[i]-1
	else:
		l[i] = l[i]+1
	i = i + val
	
print(steps)