from numpy import *

class rate:
	def __init__(self, Temperature):
		self.T = Temperature

	def Calculation(self):
		E = [0.6, 0.66, 1.45, 2.20, 1.22, 0.79, 1.16, 0.66, 1.9, 2.6, 1.22, 0.79]
		Ga_rates = array([]) 
		N_rates = array([])
		for i in range(6):
			Ga_rates = hstack([Ga_rates, exp(-E[i] / (8.617E-5*self.T)) / exp(-0.6 / (8.617E-5*self.T))])
			N_rates = hstack([N_rates, exp(-E[i+6] / (8.617E-5*self.T)) / exp(-0.6 / (8.617E-5*self.T))])

		return Ga_rates, N_rates