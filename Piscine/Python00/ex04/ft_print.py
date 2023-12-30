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


def inside_range():
	s = input('Insert a string: ')
	n = converter(input('Insert an integer: '))
	if n == 'err':
		return
	if n >= len(s):
		print('Error: index out of range')
	elif n == 1:
		print(s[n:])
	else:
		print(s[n:-(n - 1)])

if __name__=="__main__":
	inside_range()