import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	
	s = 0
	for e in gradient:
		s += e ** 2
	mag = float(np.sqrt(s))

	direction = gradient.copy()
	for i in range(len(direction)):
		if mag == 0:
			direction[i] = 0
		else:
			direction[i] /= mag
	
	descent_direction = direction.copy()
	for i in range(len(descent_direction)):
		descent_direction[i] *= -1
	
	return {
		"magnitude" : mag,
		"direction" : direction,
		"descent_direction" : descent_direction
	}


