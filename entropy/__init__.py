import entropy._entropy as _entropy

def entropy(data):
	"""Compute the Shannon entropy of the given string."""
	return _entropy.shannon_entropy(data)

if __name__ == '__main__':
	print entropy('\n'.join(file(__file__)))
