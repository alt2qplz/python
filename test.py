N = int(input())

for i in range(N):
	x = int(input())
	if x < 0:
		print('I')
	elif x < 5:
		print('II')
	elif x < 10:
		print('III')
	else:
		print('IV')