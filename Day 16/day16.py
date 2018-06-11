puzzle = open('input.txt', 'r')
commands = puzzle.readline().split(',')
prog = list('abcdefghijklmnop')

def spin(prog, n):
	start = prog[-n:]
	end = prog[:-n]
	return start + end

def exchange(prog, a, b):
	tmp = prog[a]
	prog[a] = prog[b]
	prog[b] = tmp

def partner(prog, a, b):
	indexA = prog.index(a)
	indexB = prog.index(b)
	exchange(prog, indexA, indexB)

def runDance(prog):
	for cmd in commands:
		if cmd[0] == 's':
			prog = spin(prog, int(cmd[1:]))
		elif cmd[0] == 'x':
			parts = cmd[1:].split('/')
			exchange(prog, int(parts[0]), int(parts[1]))
		elif cmd[0] == 'p':
			partner(prog, cmd[1], cmd[3])
	return prog

prog = runDance(prog)
print(''.join(prog))


# part b seems like another efficiency problem
# running any code for one billion times, will take time

# just going to hardcode it for now

'''
times = 100000000

for i in range(1000000000 - 1):
	for cmd in commands:
		if cmd[0] == 's':
			prog = spin(prog, int(cmd[1:]))
		elif cmd[0] == 'x':
			parts = cmd[1:].split('/')
			exchange(prog, int(parts[0]), int(parts[1]))
		elif cmd[0] == 'p':
			partner(prog, cmd[1], cmd[3])

	if i == times:
		print('Looped ' + times + ' times')
		times += 100000000

print(''.join(prog))

'''

# this ^ does not work, 2 min in and not reached 100 000 000 yet

# think it is good to see when it loopes
# if u find it, you can calculate what the answer is

seen = [''.join(prog)]
notSeen = True 

while notSeen:
	prog = runDance(prog)
	if ''.join(prog) in seen:
		notSeen = False
	else:
		seen.append(''.join(prog))

print(seen)
print(len(seen))

index = 1000000000 % len(seen) - 1
print(index)
print(seen[index])






