def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	sign = 1
	i = 0
	try:
		while string[i]:
			if string[i] == '-':
				sign *= -1
			elif not string[i] in dict_var:
				return False
			else:
				while string[i]:
					if string[i] in dict_var:
						n *= 10
						n += dict_var[string[i]]
					else:
						break
					i += 1
				break
			i += 1
	except IndexError:
		pass
	n *= sign
	return n

def ft_sum():
	s1 = input('Insert your first integer: ')
	n1 = converter(s1)
	if n1 == False:
		return
	s2 = input('Insert your second integer: ')
	n2 = converter(s2)
	if n2 == False:
		return
	print(n1 + n2)

if __name__=="__main__":
	ft_sum()
