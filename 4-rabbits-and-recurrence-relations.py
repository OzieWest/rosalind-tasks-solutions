n = 33
k = 4

total = 1
count = 1

for _ in range(0, n - 2):	
	currentTotal = total
	total = (total + k * count)
	count = currentTotal

print total