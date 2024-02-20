def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	sign = 1
	i = 0
	try:
		string[i]
	except IndexError:
		return 'err'
	while string[i] == '-' or string[i] == '+':
		if string[i] == '-':
			sign *= -1
		i += 1
	string = string[i:]
	for c in string:
		if c not in dict_var:
			return 'err'
		n *= 10
		n += dict_var[c]
	n *= sign
	return n

def ft_sum():
	s1 = input('Insert your first integer: ')
	n1 = converter(s1)
	if n1 == 'err':
		return
	s2 = input('Insert your second integer: ')
	n2 = converter(s2)
	if n2 == 'err':
		return
	print(n1 + n2)

if __name__=="__main__":
	ft_sum()
