# just read that some answers are over i milllion picoseconds, while my code 
# from part a) uses like a minute to get to 2000...
# Need to rethik my code completely, because this problem is 
# now an efficiency problem

def readInput():
	puzzle = open('input.txt', 'r')
	l = []
	last = 0
	for line in puzzle:
		s = line.split(': ')
		# 		 Dataformat:
		# 		 [  depth,     range  ]
		l.append([int(s[0]), int(s[1])])
		last += 1
	return l

# coming up with this equation is the real problem
# makes the "scanning" more efficient shan manually updating 
# the position one by one
def getScannerPosition(s, delay):
	return (delay + s[0]) % (2*s[1]-2)

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
