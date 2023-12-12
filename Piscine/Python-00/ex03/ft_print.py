def converter(str):
	n = 0	
	for i in str:
		n *= 10
		n += dict_var[i]
	return n


dict_var = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
s = input('Insert a string: ')
n = converter(input('Insert an integer: '))
if n >= len(s):
	print('Error: index out of range')
elif n == 0:
	print(s[n] + ' ' + s[len(s) - 1])
else:
	print(s[n] + ' ' + s[len(s) - n])