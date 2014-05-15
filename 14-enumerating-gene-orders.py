import math
import ext

value = 7

data = [i for i in range(1, value + 1)]

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):        	
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

for i in all_perms(data):
	print i