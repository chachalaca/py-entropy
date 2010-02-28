import entropy._entropy as _entropy

def entropy(data):
	"""Compute the Shannon entropy of the given string.

	Returns a floating point value indicating how many bits of entropy
	there are per octet in the string."""
	return _entropy.shannon_entropy(data)

def absolute_entropy(data):
	"""Compute the "absolute" entropy of the given string.

	The absolute entropy of a string is how many bits of information,
	total, are in the entire string. This is the same as the Shannon entropy
	multiplied by the length of the string.

	A string can be losslessly compressed to a size no smaller than its
	absolute entropy."""
	
	return entropy(data) * len(data)

def relative_entropy(data):
	"""Compute the relative entropy of the given string.

	The relative entropy is the ratio of the entropy of a string to its size,
	i.e., a measure of how well it uses space. It is, therefore, a floating
	point value on the interval (0, 1]."""

	return entropy(data) / 8

if __name__ == '__main__':
	print entropy('\n'.join(file(__file__)))
