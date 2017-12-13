def connectedWith(index):
	for n in range(0,len(pipes[index])):
		if pipes[index][n] not in connections:
			connections.append(pipes[index][n])
			connectedWith(pipes[index][n])

puzzle = open('day12Input.txt', 'r')
pipes = []
for line in puzzle:
	# remove unwanted data
	line = line.replace(' <-> ', ' ').replace(', ', ' ').replace('\n', '')
	pipe = line.split(' ')
	# Loop and add values
	pipes.append([int(pipe[n]) for n in range(1, len(pipe))])

connections = [0]
connectedWith(0)
print(len(connections))