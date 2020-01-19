import numpy as np 
import random

class Growth:
	def __init__(self, T, st, sz):
		self.size = 32
		self.T = T
		self.sampling_times = st
		self.sampling_size = sz
		self.board = np.zeros((self.size, self.size))

	def rate_calcu(self):
		E = [0.6, 0.66, 1.45, 1.22, 0.79, 1.16, 0.66, 1.9, 1.22, 0.79]
		Ga_rates = np.array([]) 
		N_rates = np.array([])
		for i in range(5):
			Ga_rates = np.hstack([Ga_rates, np.exp(-E[i] / (8.617E-5*self.T)) / np.exp(-0.6 / (8.617E-5*self.T))])
			N_rates = np.hstack([N_rates, np.exp(-E[i+5] / (8.617E-5*self.T)) / np.exp(-0.6 / (8.617E-5*self.T))])

		return Ga_rates, N_rates

	def choose_rate(self):
		rate_seq = []
		Rn = [0]
		Ga_r, N_r = self.rate_calcu()

		for i in range(self.size):
			for j in range(self.size):
				if self.board[i][j] == 1:
					if i % 2 == 0: # N
						rate = N_r
					else: 
						rate = Ga_r
			
					if i % 4 == 0:
						check_d = np.array([[-1, 0], [1, 0], [-1, 1], [0, -1], [0, 1], [-2, -1], [-2, 0], [2, -1], [2, 0]]) # row, column
					elif i % 4 == 1:
						check_d = np.array([[-1, 0], [1, 0], [1,  1], [0, -1], [0, 1], [-2, 1], [-2, 0], [2, 1], [2, 0]]) # row, column
					elif i % 4 == 2:
						check_d = np.array([[-1, 0], [1, 0], [-1, -1], [0, -1], [0, 1], [-2, 1], [-2, 0], [2, 1], [2, 0]]) # row, column					
					else:
						check_d = np.array([[-1, 0], [1, 0], [1,  -1], [0, -1], [0, 1], [-2, -1], [-2, 0], [2, -1], [2, 0]]) # row, column

					local = 0
					for m in range(3):
						local += self.board[(i + check_d[m][0]) % self.size][(j + check_d[m][1]) % self.size]

					if local > 1:
						continue

					for n in range(3, 9):
						mv_site_i = (i + check_d[n][0]) % self.size
						mv_site_j = (j + check_d[n][1]) % self.size

						if self.board[mv_site_i][mv_site_j] == 0:
							if mv_site_i % 4 == 0:
								NN_dir = np.array([[-1, 0], [1, 0], [-1, 1]]) # row, column
							elif mv_site_i % 4 == 1:
								NN_dir = np.array([[-1, 0], [1, 0], [1,  1]]) # row, column
							elif mv_site_i % 4 == 2:
								NN_dir = np.array([[-1, 0], [1, 0], [-1, -1]]) # row, column					
							else:
								NN_dir = np.array([[-1, 0], [1, 0], [1,  -1]]) # row, column
						else:
							continue

						target = 0
						for dirc in NN_dir:
							target += self.board[(i + dirc[0]) % self.size][(j + dirc[1]) % self.size]

						if local == 0:
							if target <= 2:
								Rn.extend([Rn[-1] + rate[int(target)]])
								rate_seq.append([i, j, mv_site_i, mv_site_j])
						else:
							if target <= 1:
								Rn.extend([Rn[-1] + rate[int(target)]])
								rate_seq.append([i, j, mv_site_i, mv_site_j])

		return Rn, rate_seq

	def move(self):
		self.board[int(self.size/2)][int(self.size/2)] = 1
		for i in range(self.sampling_times):
			avail = []
			print(i)
			for j in range(self.sampling_size):
				Rn, rate_seq = self.choose_rate()

				u_r = random.random()
				# u_t = random.random()

				R_i = u_r * Rn[-1]
				R_temp = sorted(Rn + [R_i])
				n_th = R_temp.index(R_i) - 1

				self.board[rate_seq[n_th][0]][rate_seq[n_th][1]] = 0
				self.board[rate_seq[n_th][2]][rate_seq[n_th][3]] = 1

			for m in range(self.size):
				for n in range(self.size):
					if self.board[m][n] == 0:
						avail.append([m, n])
			adatom = random.choice(avail)
			
			self.board[adatom[0]][adatom[1]] = 1
		return self.board

T = 500
sampling_times = 300
sampling_size = 100

run = Growth(T, sampling_times, sampling_size)
fileNameCSV = 'GaN_T%d_N%d.csv' % (T, sampling_times)
# fileNameXYZ = 'Board_T%d_N%d.xyz' % (T, sampling_times)
fileNameXYZ = '1111.xyz'

np.savetxt('%s' % (fileNameCSV), run.move(), delimiter=",")

A = 1
B = 3 * A
C = 1.732 * A
D = 1/2 * A


loca = np.genfromtxt('%s' % (fileNameCSV), delimiter=',')

f = open('%s' % (fileNameXYZ), 'w')
f.write('%d \n' % (300))

for i in range(len(loca)):
	for j in range(len(loca)):
		if loca[i][j] == 1:
			if i % 4 == 0:
				f.write('N     %f     %f     0\n' % (A * int(i/4) * 3, j * C))
			elif i % 4 == 1:
				f.write('Ga     %f     %f     0\n' % (A * (int(i/4) * 3 + 0.5), (j + 0.5) * C))
			elif i % 4 == 2:
				f.write('N     %f     %f     0\n' % (A * (int(i/4) * 3 + 1.5), (j + 0.5) * C))
			elif i % 4 == 3:
				f.write('Ga     %f     %f     0\n' % (A * (int(i/4) * 3 + 2), j * C))

f.close()

