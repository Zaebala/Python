max_val = [56,9,11,2]

def max_value(max_val):
	j = (''.join(sorted([str(i) for i in max_val], reverse=True)))
	return j
print(max_value(max_val))