def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	sign = 1
	i = 0
	try:
		while string[i]:
			if not string[i] in dict_var:
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

def ft_sum_time():
	h = converter(input('Insert hours: '))
	if h == False:
		return
	m = converter(input('Insert minutes: '))
	if m == False:
		return
	s = converter(input('Insert seconds: '))
	if s == False:
		return
	h = h * 60 * 60
	m *= 60
	print('Total seconds:', end=' ')
	print (h+m+s)

if __name__=="__main__":
	ft_sum_time()