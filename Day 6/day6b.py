from copy import deepcopy
puzzle = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5];
previous = [puzzle]
seenBefore = False
count = 0
while not seenBefore:
	# print(previous)
	count = count + 1;
	p = deepcopy(puzzle)
	maxValue = max(p)
	maxIndex = p.index(maxValue)
	p[maxIndex] = 0
	for i in range(1,maxValue+1):
		index = (maxIndex+i)%len(p)
		p[index] = p[index] + 1
	# print(previous)
	if p not in previous:
		previous.append(deepcopy(p))
	else:
		seenBefore = True;
	puzzle = p

print(len(previous))