def permutList(l):
    if not l:
		return [[]]
    res = []
    for e in l:
		temp = l[:]
		temp.remove(e)
		res.extend([[e] + r for r in permutList(temp)])
    return res

data = ['G', 'I', 'H']

print permutList(data)

#import itertools
#for a, b, c, d in itertools.product(data, repeat=4):
	#print a + b + c + d
