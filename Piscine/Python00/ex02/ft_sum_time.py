def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	i = 0
	try:
		string[i]
	except IndexError:
		return 'err'
	while string[i] == '+':
		i += 1
	string = string[i:]
	for c in string:
		if c not in dict_var:
			return 'err'
		n *= 10
		n += dict_var[c]
	return n

def ft_sum_time():
	h = converter(input('Insert hours: '))
	if h == 'err':
		return
	m = converter(input('Insert minutes: '))
	if m == 'err':
		return
	s = converter(input('Insert seconds: '))
	if s == 'err':
		return
	h = h * 60 * 60
	m *= 60
	print('Total seconds:', end=' ')
	print (h+m+s)

if __name__=="__main__":
	ft_sum_time()