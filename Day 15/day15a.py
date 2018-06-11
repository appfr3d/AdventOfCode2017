# [generator A, generator B]
gen = [679, 771]
multi = [16807, 48271]

count = 0

# loop 40 million times
for _ in range(40000000):

	# generate new numbers
	for i in [0,1]:
		gen[i] = (gen[i] * multi[i]) % 2147483647

	# get the 16 first numbers in the binary version og the numbers
	a = bin(gen[0])[2:].zfill(16)[-16:]
	b = bin(gen[1])[2:].zfill(16)[-16:]

	if a == b:
		count += 1

print(count)