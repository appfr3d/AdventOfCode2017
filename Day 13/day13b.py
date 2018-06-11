# just read that some answers are over i milllion picoseconds, while my code 
# uses like a minute to get to 2000...
# Need to rethik my code completely, because this problem is 
# now an efficiency problem

def readInput():
	puzzle = open('input.txt', 'r')
	l = []
	last = 0
	for line in puzzle:
		s = line.split(': ')
		# Dataformat:
		# [depth, range]

		l.append([int(s[0]), int(s[1])])
		last += 1
	return l

# returns True if you are chaught, False if you are not
def chaughtByScanner(scanner, pos):
	if not scanner[pos][0] == 0:
		if scanner[pos][1] == 0:
			return True
	return False

def getScannerPosition(s, delay):
	return (delay + s[0]) % (2*s[1]-2)



def moveOneScanner(s):
	if not s[0] == 0:
		if s[2]: 	s[1] += 1
		else: 		s[1] -= 1

		if s[1] == 0 or s[1] == s[0]-1:
			s[2] = not s[2]


scanner = readInput()
chaught = True
delay = 10

while chaught:
	delay += 1
	chaught = False
	for s in scanner:
		if getScannerPosition(s, delay) == 0:
			chaught = True
			break

print(delay)
