import math

	
					
class Problemas():

	def primos(self, m):
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

	def fun(self, m):
		if m==1:
			return 1

		elif m == 3:
			return 3

		elif m % 2 == 0:
			m = m/2
			return Problemas.fun(self,m)

		elif (m % 4 == 1) and (m>1):
			m = (m-1)/4
			return (2*Problemas.fun(self,(2*m)+1)) - Problemas.fun(self,m)

		else:
			m = (m-3)/4
			return (3*Problemas.fun(self,(2*m)+1)) - (2*Problemas.fun(self,m))		

	def problema1(self):
		pass

	def problema2(self):
		pass
	
	def problema3(self, m):
		""" Devuelve una lista con todos los enteros n < m tales que n tiene exactamente dos divisores primos"""
		pr = Problemas.primos(self,m)
		c=0
		resultado = [4]
		for n in range(5,m+1):
			aux = n
			c =0
			while not aux == 1:
				for p in pr:
					if (p < aux ) and (aux%p ==0):
						c +=1
						aux = aux/p
					elif aux == p:
						c += 1
						aux = 1	
			if c == 2:
				resultado.append(n)

		return resultado

	def problema4(self,m):
		""" Devuelve el valor de S(m) como definido en el problema 4"""
		n = (m // 4) -1
		Sum = 0
		for i in range(0,n+1):
			Sum = Sum + (6*Problemas.fun(self,(2*n)+1)) - Problemas.fun(self,n)
		
		t = 4*m
		while t<= m :
			Sum = Sum + Problemas.fun(self,t)
			t +=1

		return Sum				