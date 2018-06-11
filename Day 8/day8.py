# read the puzzle
puzzle = open('input.txt', 'r')

# define the operators
operator = {	
	'>=':  (lambda x,y: x>=y), 
	'<=':  (lambda x,y: x<=y),
	'>' :  (lambda x,y: x>y ),
	'<' :  (lambda x,y: x<y ),
	'!=':  (lambda x,y: x!=y),
	'==':  (lambda x,y: x==y),
	'dec': (lambda x,y: x-y ),
	'inc': (lambda x,y: x+y )
}

registers = {}
maxVal = 0

# loop through each line in puzzle input
for line in puzzle:
	parts = line.split(' ')

	# initialize the registers if they are already
	if not parts[0] in registers:
		registers[parts[0]] = 0
	if not parts[4] in registers:
		registers[parts[4]] = 0

	#  0   1   2  3   4  5  6
	# gug dec 188 if zpw >= 8

	# check condition
	if operator[parts[5]](registers[parts[4]], int(parts[6])):

		# update set if needed
		val = operator[parts[1]](registers[parts[0]], int(parts[2]))
		registers[parts[0]] = val
		if val > maxVal:
			maxVal = val


print(max(registers.values()))
print(maxVal)




