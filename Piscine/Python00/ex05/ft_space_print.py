s = input('Insert a string: ')
s_len = len(s)
if s_len < 20:
	print(' '* (20 - s_len), end='')
	print(s)
else:
	i = s_len - 20
	while i < s_len:
		print(s[i], end='')
		i += 1
	print()
