import sys

num = 1
try:
	f1 = float(sys.argv[1])
	f2 = float(sys.argv[2])
except (IndexError, ValueError) as e:
	num = 0
if num == 0:
	pass
elif f1 > f2:
	print(f'{f1} is greater than {f2}')
elif f1 == f2:
	print(f'{f1} is equal to {f2}')
else:
	print(f'{f1} is less than {f2}')
