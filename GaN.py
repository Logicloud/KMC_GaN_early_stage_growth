from numpy import * 
from rate_calcu import rate

class Growth:
	def __init__(self):
		self.size = self.size
		self.board = zeros((self.size, self.size))


	def choose_rate(self):
		for i in range(self.size): # row
			for j in range(self.size): # column
				if self.board[i][j] == 1:
					if i % 4 == 0:
						check_d = array([[0, -1], [0, 1], [1, -1], [-1, 0], [1, 0], [-1, -1], [0, -1], [-1, 1], [0, 1]]) # column, row
					elif i % 4 == 1:
						check_d = array([[0, -1], [0, 1], [1,  1], [-1, 0], [1, 0], [1, -1], [0, -1], [1, 1], [0, 1]]) # column, row
					elif i % 4 == 2:
						check_d = array([[0, -1], [0, 1], [-1, -1], [-1, 0], [1, 0], [1, -1], [0, -1], [1, 1], [0, 1]]) # column, row					
					else:
						check_d = array([[0, -1], [0, 1], [-1,  1], [-1, 0], [1, 0], [-1, -1], [0, -1], [-1, 1], [0, 1]]) # column, row

				local = 0
				for m in range(3):
					if self.board[(i + check_d[m][1]) % self.size][(j + check_d[m][0]) % self.size] == 1:
						local += 1

				for n in range(3, 9):
					mv_site_i = (i + check_d[n][1]) % self.size
					mv_site_j = (j + check_d[n][0]) % self.size
					if self.board[mv_site_i][mv_site_j] == 0:
						if mv_site_i % 4 == 0:
							check_d = array([[0, -1], [0, 1], [1, -1], [-1, 0], [1, 0], [-1, -1], [0, -1], [-1, 1], [0, 1]]) # column, row
						elif mv_site_i % 4 == 1:
							check_d = array([[0, -1], [0, 1], [1,  1], [-1, 0], [1, 0], [1, -1], [0, -1], [1, 1], [0, 1]]) # column, row
						elif mv_site_i % 4 == 2:
							check_d = array([[0, -1], [0, 1], [-1, -1], [-1, 0], [1, 0], [1, -1], [0, -1], [1, 1], [0, 1]]) # column, row					
						else:
							check_d = array([[0, -1], [0, 1], [-1,  1], [-1, 0], [1, 0], [-1, -1], [0, -1], [-1, 1], [0, 1]]) # column, row

						target = 0
						for m in range(3):
							if self.board[(i + check_d[m][1]) % self.size][(j + check_d[m][0]) % self.size] == 1:
								target += 1

	def build_rate(self):
		pass




A = 1 # need change 
B = 2 # need change 

T = 490
rates = rate(T)
Ga_rates, N_rates = rates.Calculation()
print(Ga_rates)


sampling_times = 100
sampling_size = 100

# for i in range(sampling_times):
# 	for j in range(sampling_size):
# 		# how it works