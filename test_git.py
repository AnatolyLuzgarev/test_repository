import random
import math





def sqrt_approx(x):
	appr = 1 - x/2
	return appr

def mult_vectors(v_1, v_2):
	result = 0
	for i in range(len(v_1)):
		result = result + v_1[i]*v_2[i]
	return result

