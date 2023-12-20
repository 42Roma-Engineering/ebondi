def converter(string):
	dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
	n = 0
	sign = 1
	i = 0
	try:
		string[i]
	except IndexError:
		raise KeyError
	while string[i] == '-' or string[i] == '+':
		if string[i] == '-':
			sign *= -1
		i += 1
	string = string[i:]
	for c in string:
		if c not in dict_var:
			raise KeyError
		n *= 10
		n += dict_var[c]
	n *= sign
	return n

if __name__=="__main__":
	try:
		min_len = converter(input('Insert an integer: '))
		f = open('words.txt', 'r')
		words = []
		for line in f:
			line = line.rstrip('\n')
			if len(line) > min_len:
				if not words:
					words.append(line)
					continue
				i = 0
				size = len(words)
				while i < size:
					if line < words[i]:
						words.insert(i, line)
						break
					elif i == size - 1:
						words.append(line)
					i += 1
		print(f'The words longer than {min_len} are the following:')
		for w in words:
			print (w)
	except KeyError:
		pass