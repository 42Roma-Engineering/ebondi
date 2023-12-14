import sys

def all_to_lower(string):
	low_dict = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
    'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
    'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
    'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
    'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y',
    'Z': 'z'
	}
	size = len(string)
	i = 0
	new = ''
	while i < size:
		if string[i] in low_dict:
			new += low_dict[string[i]]
		else:
			new += string[i]
		i += 1
	return new	

def char_sort_dict(string):
	min = string[0]
	for c in string:
		if c < min:
			min = c
	c_count = {}
	c_count.setdefault(min, 0)
	not_set = '' + min
	min = ''
	i = 0
	size = len(string)
	while i < size:
		if string[i] not in not_set:
			min = string[i]
			for ch in string:
				if ch < min and ch not in not_set:
					min = ch
			not_set += min
			c_count.setdefault(min, 0)
			i = 0
			continue
		i += 1
	return c_count


def ft_char_count(string):
	string = all_to_lower(string)
	c_count = char_sort_dict(string)

	for c in string:
		ret = c_count.get(c, 0)
		c_count[c]=ret+1
	print('Char count:')
	for key, value in c_count.items():
		print(key, end='')
		print(' = ', end='')
		print(value)

if __name__=="__main__":
	if len(sys.argv) > 1:
		ft_char_count(sys.argv[1])
	else:
		print('Error! No string given')