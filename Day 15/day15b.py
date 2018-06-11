# [generator A, generator B]
gen = [679, 771]
multi = [16807, 48271]
count = 0
loops = 0
done = 1000000
compare = [[], []]

print('Starting to add...')

# loop until both generators have made 5 million integers
while len(compare[0]) < 5000000 or len(compare[1]) < 5000000:
	# generate new numbers
	gen[0] = (gen[0] * multi[0]) % 2147483647
	gen[1] = (gen[1] * multi[1]) % 2147483647

	# only add to comparison it it meets the requrements
	if gen[0]%4 == 0:
		compare[0].append(bin(gen[0])[2:].zfill(16)[-16:])

	if gen[1]%8 == 0:
		compare[1].append(bin(gen[1])[2:].zfill(16)[-16:])

	# print progress
	if loops == done: 
		print(str(done) + ' loops done')
		done += 1000000

	loops += 1

print('Done adding, starting to compare...')

for i in range(5000000):
	if compare[0][i] == compare[1][i]:
		count += 1


print('Comparing done, the judge counted: ' + str(count))
