puzzleInput = '70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41'
# puzzleInput = '1,2,4'
lengths = [ord(x) for x in puzzleInput] + [17, 31, 73, 47, 23]

# modified copy of part a
l = 256
sparseHash = [*range(l)]
pos = 0
stepSize = 0

for _ in range(64):
	for length in lengths:
		# Reverse a part of the list
		if pos+length < l:
			# If the part does not wrap arpound
			sparseHash[pos:pos+length] = sparseHash[pos:pos+length][::-1]
		else:
			# If the part does wrap around, make a new list from
			# those parts, and reverse it
			tmp = (sparseHash[pos:] + sparseHash[:(pos+length)%l])[::-1]

			# insert the parts of the list where it belongs
			sparseHash[pos:] = tmp[:(len(sparseHash)-pos)]
			sparseHash[:(pos+length)%l] = tmp[(len(sparseHash)-pos):]


		# update current position and stepsize
		pos = (pos+stepSize+length)%l
		stepSize += 1


splitted = [sparseHash[i*16: (i*16) + 16] for i in range(16)]
denseHash = []
for i in range(16):
	denseHash.append(splitted[i][0])
	for j in range(1,16):
		denseHash[i] ^= splitted[i][j]


s = ''
s = [s + '%x'%x for x in denseHash]

# Add zero if needed
for h in range(len(s)):
	if len(s[h])==1:
		s[h] = '0' + s[h]

print(''.join(s))


