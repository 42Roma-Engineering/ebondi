import sys

def ft_max():
	if (len(sys.argv) == 4):
		try:
			max = float(sys.argv[1])
			n2 = float(sys.argv[2])
			n3 = float(sys.argv[3])
		except (IndexError, ValueError) as e:
			return
		if (n2 > max):
			max = n2
		if (n3 > max):
			max = n3
		print('The max is:', end=' ')
		print(max)
	else:
		print('Error! Usage: python3 ft_max.py <x> <y> <z>')

if __name__=="__main__":
	ft_max()