def connectedWith(index):
	for n in range(0,len(pipes[index])):
		if pipes[index][n] not in groups[-1]:
			groups[-1].append(pipes[index][n])
			connectedWith(pipes[index][n])

puzzle = open('day12Input.txt', 'r')
pipes = []
for line in puzzle:
	# remove unwanted data
	line = line.replace(' <-> ', ' ').replace(', ', ' ').replace('\n', '')
	pipe = line.split(' ')
	# Loop and add values
	pipes.append([int(pipe[n]) for n in range(1, len(pipe))])

# initialize values
groups = []
groups.append([])
connectedWith(0)

# for each program (after zero)
for program in range(1,len(pipes)):
	# assume that it is not in a group
	inGroup = False
	# check if it is in a group
	for i in range(0,len(groups)):
		# if not, make a new group
		if program in groups[i]:
			inGroup = True
	if not inGroup:
		groups.append([])
		connectedWith(program)

print(len(groups))