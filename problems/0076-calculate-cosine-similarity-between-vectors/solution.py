import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	dot = 0
	v1_l2 = 0
	v2_l2 = 0
	for i in range(len(v1)):
		dot += v1[i] * v2[i]
		v1_l2 += v1[i] ** 2
		v2_l2 += v2[i] ** 2
	v1_l2 = np.sqrt(v1_l2)
	v2_l2 = np.sqrt(v2_l2)
	
	return (dot / (v1_l2 * v2_l2))