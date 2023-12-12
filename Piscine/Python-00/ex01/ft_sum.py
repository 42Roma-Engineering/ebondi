def converter(string):
	n = 0
	sign = 1
	i = 0
	try:
		while string[i]:
			if string[i] == '-':
				sign *= -1
			elif not string[i] in dict_var:
				i += 1
				continue
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


dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
s1 = input('Insert your first integer: ')
s2 = input('Insert your second integer: ')
n1 = converter(s1)
n2 = converter(s2)
print(n1 + n2)
