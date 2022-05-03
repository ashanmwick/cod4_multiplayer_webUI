def get_factors(input_num,limits=100):
	factors=[]
	for i in range(1,limits+1):
		rest=input_num%i
		if rest==0:
			factors.append(i)
		else:
			pass

	return factors
