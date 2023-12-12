import sys
def float_convert(string):
	try:
		if (string[0]):
			pass
	except TypeError:
		return string
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	i = 0
	n = 0
	sign = 1
	try:
		while string[i] == '-':
			sign *= -1
			i += 1
		while string[i]:
			n *= 10
			n += dict_var[string[i]]
			i += 1
			if string[i] == '.':
				i += 1
				div = 10
				while string[i]:
					n += dict_var[string[i]] / div
					div *= 10
					i += 1
				break
	except IndexError:
		pass
	n *= sign
	return n

def my_min(a = '0', b = '0', c = '0'):
	if a == 0 and b == 0 and c == 0:
		return 0
	try:
		min = float_convert(a)
		n2 = float_convert(b)
		n3 = float_convert(c)
	except KeyError:
		return -1
	if (n2 < min):
		min = n2
	if (n3 < min):
		min = n3
	return min

if __name__=="__main__":
	if (len(sys.argv) == 4):
		mi = my_min(sys.argv[1], sys.argv[2], sys.argv[3])
		if mi != -1:
			print('The min is:', end=' ')
			print(mi)
	else:
		print('Error! Usage: python3 ft_min.py <x> <y> <z>')