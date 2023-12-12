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
	print(sys.argv[1] + ' is greater than ' + sys.argv[2])
elif f1 == f2:
	print(sys.argv[1] + ' is equal to ' + sys.argv[2])
else:
	print(sys.argv[1] + ' is less than ' + sys.argv[2])
