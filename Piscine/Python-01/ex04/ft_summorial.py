import sys

def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	sign = 1
	i = 0
	try:
		while string[i]:
			if string[i] == '-':
				sign *= -1
			else:
				while string[i]:
					n *= 10
					n += dict_var[string[i]]
					i += 1
				break
			i += 1
	except IndexError:
		pass
	n *= sign
	return n

if __name__=="__main__":
	if (len(sys.argv) == 2):
		try:
			n = converter(sys.argv[1])
			if n >= 0:
				sum = 0
				n += 1
				i = 0
				while i < n:
					sum += i
					i += 1
				print('The sum is:', end=' ')
				print(sum)
			else:
				print('Error! n must be >=0')
		except KeyError:
			pass
	else:
		print('Error! Usage: python3 ft_summorial.py <n>')