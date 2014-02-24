from pandas import Series

def sign(x):
    if x>=0: return 1
    else: return -1
    
def PLA(sample):
	E = True
	w = Series([0, 0., 0.])
	while E:
		E = False
		for i in range(len(sample)):
			x1, x2, y = sample.ix[i].values
			x = Series([1, x1, x2])
			if(sign((w*x).sum()) != y): 
				E = True
				w = w + y*x
				break
	return w

