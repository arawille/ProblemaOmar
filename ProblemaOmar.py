import math

def primos(m):
	"""Devuelve los primos desde el 2 hasta m usando la Criba de Eratóstenes"""
	criba = [[n,0] for n in range(2,m+1)]
	i =0
	while i <= m-2:
		if criba[i][1] == 0:
			for n in range(i+1, m-1):
				if (criba[n][0] % criba[i][0]== 0) and (criba[n][1]==0):
					criba[n][1]= 1
		i+=1
	
	pr = [2]
	for t in range(3,m+1):
		if criba[t-2][1]==0:
			pr.append(t)

	return pr		
		
			


class Problemas:

	def __init__(self):
		self.var = [100000, 1777, 1855, 10**8, 3**37]

	def problema1(self):
		pass

	def problema2(self):
		pass
	
	def problema3(self):
		pass

	def problema4(self):
		pass

m = 10**8
print(primos(m))		