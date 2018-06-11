def readInput():
	puzzle = open('input.txt', 'r')
	l = []
	last = 0
	for line in puzzle:
		s = line.split(': ')

		# Dataformat:
		# [range, position counter, isMovingDown]
		while last < int(s[0]):
			l.append([0,0, True])
			last += 1

		l.append([int(s[1]), 0, True])
		last += 1
	return l



def checkScanner(scanner, pos):
	if not scanner[pos][0] == 0:
		if scanner[pos][1] == 0:
			# scanner is on the top
			# print(scanner[pos])
			return pos * scanner[pos][0]
	return 0


def moveScanner(scanner):
	for s in scanner:
		# print(s)
		if not s[0] == 0:
			if s[2]: 	s[1] += 1
			else: 		s[1] -= 1

			if s[1] == 0 or s[1] == s[0]-1:
				s[2] = not s[2]

# part a
scanner = readInput()
pos = 0
severity = 0

while pos < len(scanner):
	severity += checkScanner(scanner, pos)
	moveScanner(scanner)
	pos += 1

print(severity)

