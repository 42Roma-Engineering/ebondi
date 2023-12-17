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

def print_words():
	file = input('Insert file name: ')
	try:
		f = open(file, 'r')
	except FileNotFoundError:
		print('Error! The specified file does not exist!')
		return
	try:
		min_len = converter(input('Insert an integer: '))
	except KeyError:
		return
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

if __name__=="__main__":
	print_words()