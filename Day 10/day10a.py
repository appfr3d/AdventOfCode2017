l = 256	# 5 for example
aList = [*range(l)]
pos = 0
stepSize = 0

# puzzle input
lengths = [70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41] 

# example
# lengths = [3, 4, 1, 5]	


for length in lengths:
	# Reverse a part of the list
	if pos+length < l:
		# If the part does not wrap arpound
		aList[pos:pos+length] = aList[pos:pos+length][::-1]
	else:
		# If the part does wrap around, make a new list from
		# those parts, and reverse it
		tmp = (aList[pos:] + aList[:(pos+length)%l])[::-1]

		# insert the parts of the list where it belongs
		aList[pos:] = tmp[:(len(aList)-pos)]
		aList[:(pos+length)%l] = tmp[(len(aList)-pos):]


	# update current position and stepsize
	pos = (pos+stepSize+length)%l
	stepSize += 1


print(aList)
print(aList[0]*aList[1])