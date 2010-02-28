from entropy._entropy import shannon_entropy

def entropy(data):
	"""Compute the Shannon entropy of the given string."""
	return shannon_entropy(data)

if __name__ == '__main__':
	print entropy('\n'.join(file(__file__)))
