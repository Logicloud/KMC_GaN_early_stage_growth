import numpy as np

A = 1
B = 3 * A
C = 1.732 * A
D = 1/2 * A


loca = np.genfromtxt('board.csv', delimiter=',')
print loca

f = open('GaN1000_1.xyz', 'w')
f.write('%d \n' % (100))

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
